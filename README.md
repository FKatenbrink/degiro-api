# DeGiro-API

This repository contains a non-official DeGiro API library for Python.

## Usage

```
from degiro import DeGiro

degiro = DeGiro()
degiro.login(DEGIRO_USERNAME, DEGIRO_PASSWORD)
products = degiro.search_products('Vanguard', product_types=[Product.Type.ETF])
print(products)
```

For more examples, see [examples](./examples).
