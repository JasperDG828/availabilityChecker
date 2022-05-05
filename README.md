# Availability checker

A quick availability checker to see the availability of products like the Xbox Series X and notify the user when available.

## Usage

You can configure the whole script in config.json:

### Products

You can add products to the script by adding a dictionary to the products-array. This dictionary should include:

- `Name`, A name to identify this product
- `URL`, The URL of this product
- `notAvailable`, Text on the website that will only be displayed when the product isn't available
- `lastAvailability`, You don't need to care a lot about this, make this false when you set everything up, and the script will enable it once the product is available

For example:

```json
"products": [
      {
          "Name": "Xbox Series X on bol.com",
          "URL": "https://www.bol.com/be/nl/p/xbox-series-x-console/9300000003688723/?referrer=socialshare_pdp_www",
          "notAvailable": "Niet leverbaar",
          "lastAvailability": false
      }]
```

### Other settings

- `checkInterval`: The time in seconds between checking the availability. Default: `10`
- `colors`: Whether to use colors in the terminal.
  Default: `true`
- `columnWidth`: The width of the terminal. Default: `50`
- `notification`: Whether to notify the user when a product is available. Default: `true`
