# Ecommerce-site-scraping
A scrapper made using Scrapy in python to scrap an e-commerce site ([seamsfriendly.com](https://in.seamsfriendly.com/)) to get all listings of shorts

The output files (in json and csv formats) include:
- Title of product
- Description_1
- Description_2
- Price
- List of image urls of all available pictures

To scrape:
```
scrapy crawl shorts -O filename.extension
```
