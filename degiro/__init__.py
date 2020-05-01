import requests
import logging
import json
from datetime import datetime, timedelta

from .utils import pretty_json
from .client_info import ClientInfo
from .product import Product

class DeGiro:
  __LOGIN_URL           = 'https://trader.degiro.nl/login/secure/login'
  __PRODUCT_SEARCH_URL  = 'https://trader.degiro.nl/product_search/secure/v5/products/lookup'
  __PRODUCT_INFO_URL    = 'https://trader.degiro.nl/product_search/secure/v5/products/info'
  __CLIENT_INFO_URL     = 'https://trader.degiro.nl/pa/secure/client'
  __TRANSACTIONS_URL    = 'https://trader.degiro.nl/reporting/secure/v4/transactions'
  __ORDERS_URL          = 'https://trader.degiro.nl/reporting/secure/v4/order-history'

  __GET_REQUEST = 0
  __POST_REQUEST = 1

  def __init__(self):
    self.logger = logging.getLogger(self.__class__.__name__)

  def __request(self, url, payload=None, request_type=__GET_REQUEST, data=None, json=None, error_message='An error occurred.'):
    if request_type == DeGiro.__GET_REQUEST:
      response = requests.get(url, params=payload)
    elif request_type == DeGiro.__POST_REQUEST:
      header = {'content-type': 'application/json'}
      response = requests.post(url, headers=header, params=payload, data=data, json=json)
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
    login_response = self.__request(DeGiro.__LOGIN_URL, json=login_payload, request_type=DeGiro.__POST_REQUEST, error_message='Could not login.')
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

  def productsByIds(self, ids):
    product_search_payload = {
      'intAccount': self.client_info.account_id,
      'sessionId': self.session_id
    }
    return self.__request(DeGiro.__PRODUCT_INFO_URL, product_search_payload, request_type=DeGiro.__POST_REQUEST,
                          data=json.dumps([str(id) for id in ids]), error_message='Could not get product info.')['data']


  def transactions(self, from_date, to_date, group_transactions=False):
    transactions_payload = {
      'fromDate': from_date.strftime('%d/%m/%Y'),
      'toDate': to_date.strftime('%d/%m/%Y'),
      'group_transactions_by_order': group_transactions,
      'intAccount': self.client_info.account_id,
      'sessionId': self.session_id
    }
    return self.__request(DeGiro.__TRANSACTIONS_URL, transactions_payload, error_message='Could not get transactions.')['data']

  def orders(self, from_date, to_date):
    orders_payload = {
      'fromDate': from_date.strftime('%d/%m/%Y'),
      'toDate': to_date.strftime('%d/%m/%Y'),
      'intAccount': self.client_info.account_id,
      'sessionId': self.session_id
    }
    # The DeGiro API requires the time span to be max 90 days, otherwise it returns orders between `fromDate` and `fromDate + 90 days`.
    if (toDate - fromDate).days > 90:
      raise Exception('The DeGiro API requires the time span to be max 90 days.')

    return self.__request(DeGiro.__ORDERS_URL, orders_payload, error_message='Could not get orders.')['data']
