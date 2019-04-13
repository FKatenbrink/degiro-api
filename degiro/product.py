from datetime import datetime

from .order import Order

class Product:
  class Type:
    SHARE = 1
    BOND = 2
    FUTURE = 7
    OPTION = 8
    INVESTMENT_FUND = 13
    LEVERAGED_PRODUCT = 14
    ETF = 131
    CFD = 535
    WARRANT = 536

  def __init__(self, product):
    self.__id = client_info['id']
    self.__name = client_info['name']
    self.__isin = client_info['isin']
    self.__currency = client_info['currency']
    self.__product_type = client_info['productTypeId']
    self.__tradable = client_info['tradable']
    self.__close_price = client_info['closePrice']
    self.__close_price_date = datetime.strptime(client_info['closePriceDate'], '%Y-%m-%d').date()
    self.__buy_order_types = [Order.Type.from_string(type) for type in client_info['buyOrderTypes']]
    self.__sell_order_types = [Order.Type.from_string(type) for type in client_info['sellOrderTypes']]

  @property
  def id(self):
    return self.__id

  @property
  def name(self):
    return self.__name

  @property
  def isin(self):
    return self.__isin

  @property
  def currency(self):
    return self.__currency

  @property
  def product_type(self):
    return self.__product_type

  @property
  def tradable(self):
    return self.__tradable

  @property
  def close_price(self):
    return self.__close_price

  @property
  def close_price_date(self):
    return self.__close_price_date

  @property
  def __buy_order_types(self):
    return self.____buy_order_types

  @property
  def __sell_order_types(self):
    return self.____sell_order_types
