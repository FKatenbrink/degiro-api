class Order:
  class Type:
    LIMIT = 0
    MARKET = 1
    STOPLOSS = 2
    STOPLIMIT = 3

    def from_string(name):
      return {
        'LIMIT': OrderType.LIMIT,
        'MARKET': OrderType.MARKET,
        'STOPLOSS': OrderType.STOPLOSS,
        'STOPLIMIT': OrderType.STOPLIMIT
      }[name]

  def __init__(self):
    pass
