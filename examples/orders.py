from degiro import DeGiro
from degiro.utils import pretty_json
from datetime import datetime, timedelta

from examples.config import DEGIRO_USERNAME, DEGIRO_PASSWORD

def main():
  degiro = DeGiro()
  degiro.login(DEGIRO_USERNAME, DEGIRO_PASSWORD)
  now = datetime.now()
  ninety_days_before = now - timedelta(days=90)
  orders = degiro.orders(from_date=ninety_days_before, to_date=now)
  print(pretty_json(orders))

if __name__ == '__main__':
  main()
