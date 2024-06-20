import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    
    custom_settings = {
        "DOWNLOAD_HANDLERS": {
            "http": "scrapy_impersonate.ImpersonateDownloadHandler",
            "https": "scrapy_impersonate.ImpersonateDownloadHandler",
        },
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
    }

    def start_requests(self):
        for browser in ["chrome123"]:
            yield scrapy.Request(
                "https://www.tesco.com/groceries/en-GB/products/313737462",
                dont_filter=True,
                meta={"impersonate": browser},
            )

    def parse(self, response):
       print(response.text)