from degiro import DeGiro
from degiro.product import Product
from degiro.utils import pretty_json

from examples.config import DEGIRO_USERNAME, DEGIRO_PASSWORD

def main():
  degiro = DeGiro()
  degiro.login(DEGIRO_USERNAME, DEGIRO_PASSWORD)
  products = degiro.search_products('Vanguard', product_types=[Product.Type.ETF])
  print(pretty_json(products))

if __name__ == '__main__':
  main()
