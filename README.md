# DeGiro-API

This repository contains an unofficial DeGiro API wrapper for Python.

## Usage

```
from degiro import DeGiro

degiro = DeGiro()
degiro.login(DEGIRO_USERNAME, DEGIRO_PASSWORD)
products = degiro.search_products('Vanguard', product_types=[Product.Type.ETF])
print(products)
```

For more examples, see [examples](./examples).
