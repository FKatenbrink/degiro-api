from degiro import DeGiro
from degiro.utils import pretty_json
from datetime import datetime

from examples.config import DEGIRO_USERNAME, DEGIRO_PASSWORD

def main():
  degiro = DeGiro()
  degiro.login(DEGIRO_USERNAME, DEGIRO_PASSWORD)
  transactions = degiro.transactions(from_date=datetime.strptime('2000-01-01', '%Y-%m-%d'), to_date=datetime.now())
  print(pretty_json(transactions))

if __name__ == '__main__':
  main()
