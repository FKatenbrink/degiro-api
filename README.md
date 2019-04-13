# degiro-api

This repository contains an unofficial DeGiro API module for Python.

## Install

```
pip install degiro-api
```

## Usage

```
from degiro import DeGiro
from degiro.product import Product

from config import DEGIRO_USERNAME, DEGIRO_PASSWORD

degiro = DeGiro()
degiro.login(DEGIRO_USERNAME, DEGIRO_PASSWORD)
products = degiro.search_products('Vanguard', product_types=[Product.Type.ETF])
print(f'{products[0]["name"]}: {products[0]["isin"]}')

```

For more examples, see [examples](./examples).

## Logging

The module uses [logging](https://docs.python.org/3/library/logging.html). It should be adjusted as a project-wide modification.
