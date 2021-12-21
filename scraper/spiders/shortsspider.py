import scrapy

#creating the spider 'shorts'
class shorts_spider(scrapy.Spider):
    name="shorts"
    page_num=2
    start_urls = [
        'https://in.seamsfriendly.com/collections/shorts',
    ]
    # function for parsing through each page of listing
    def parse(self, response):
        # opening each item on a page
        item_link = response.css('#shopify-section-collection-template section div.CollectionMain div.CollectionInner div.CollectionInner__Products div.ProductListWrapper div div div div a::attr(href)').getall()
        yield from response.follow_all(item_link, self.parse_item)

        #to go to next page if there are items on current page
        if len(item_link) != 0:
            next_link = 'https://in.seamsfriendly.com/collections/shorts?page={}'.format(self.page_num)
            self.page_num+=1
            yield scrapy.Request(next_link,callback=self.parse)

    #funtion for parsing through pages of each item
    def parse_item(self, response):
        yield{
            "Title" : response.css("#shopify-section-product-template section div.Product__Wrapper div.Product__InfoWrapper div.Product__Info div div.ProductMeta div.flexbax h1::text").get().replace('\n', ''),
            "Description_1" : response.css("#shopify-section-product-template section div.Product__Wrapper div.Product__InfoWrapper div.Product__Info div div.ProductMeta__Description div.Rte p:nth-child(1) strong::text").get(),
            "Description_2" : response.css("#shopify-section-product-template section div.Product__Wrapper div.Product__InfoWrapper div.Product__Info div div.ProductMeta__Description div.Rte ul li::text").getall(),
            "Price" : response.css("#shopify-section-product-template section div.Product__Wrapper div.Product__InfoWrapper div.Product__Info div div.ProductMeta div.flexbax div div span.ProductMeta__Price.Price.u-h4::text").get().replace('\u20b9', ''),
            "Image_urls" : list(map(lambda x: 'https:'+x, response.css("#shopify-section-product-template section div.Product__Wrapper div.Product__Gallery.Product__Gallery--stack.Product__Gallery--withThumbnails div.Product__SlideshowNav.Product__SlideshowNav--thumbnails div a img::attr(src)").getall()))
        }
