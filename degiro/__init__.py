import requests
import logging

from .utils import pretty_json
from .client_info import ClientInfo
from .product import Product

class DeGiro:
  __LOGIN_URL           = 'https://trader.degiro.nl/login/secure/login'
  __PRODUCT_SEARCH_URL  = 'https://trader.degiro.nl/product_search/secure/v5/products/lookup'
  __CLIENT_INFO_URL     = 'https://trader.degiro.nl/pa/secure/client'

  __GET_REQUEST = 0
  __POST_REQUEST = 1

  def __init__(self):
    self.logger = logging.getLogger(self.__class__.__name__)

  def __request(self, url, payload, request_type=__GET_REQUEST, error_message='An error occurred.'):
    if request_type == DeGiro.__GET_REQUEST:
      response = requests.get(url, params=payload)
    elif request_type == DeGiro.__POST_REQUEST:
      response = requests.post(url, json=payload)
    else:
      raise Exception(f'Unknown request type: {request_type}')

    if response.status_code != 200:
      raise Exception(f'{error_message} Response: {response.text}')
    self.logger.debug(pretty_json(response.json()))
    return response.json()

  def login(self, username, password):
    login_payload = {
      'username': username,
      'password': password,
      'isPassCodeReset': False,
      'isRedirectToMobile': False
    }
    login_response = self.__request(DeGiro.__LOGIN_URL, login_payload, request_type=DeGiro.__POST_REQUEST, error_message='Could not login.')
    self.session_id = login_response['sessionId']

    client_info_payload = { 'sessionId': self.session_id }
    client_info_response =  self.__request(DeGiro.__CLIENT_INFO_URL, client_info_payload, error_message='Could not get client info.')
    self.client_info = ClientInfo(client_info_response['data'])

  def search_products(self, searchText, limit=7, product_types=None):
    product_search_payload = {
      'searchText': searchText,
      'limit': limit,
      'offset': 0,
      'intAccount': self.client_info.account_id,
      'sessionId': self.session_id
    }

    products = self.__request(DeGiro.__PRODUCT_SEARCH_URL, product_search_payload, error_message='Could not get products.')['products']
    if product_types:
      return [p for p in products if p['productTypeId'] in product_types]
    else:
      return products
