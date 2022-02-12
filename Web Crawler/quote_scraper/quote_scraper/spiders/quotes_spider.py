# In scrapy we refer to the thing that will crawl the web for us as SPIDERS
import scrapy


class QuotesSpider(scrapy.Spider):

    name = "quotes_spider"  # The name of the spider

    def start_requests(self):

        urls = [
            "http://quotes.toscrape.com/page/1",
        ]

        for url in urls:
            # generator function, yields the request
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        page = response.url.split("/")[-2]
        filename = f"quotes{page}.html"

        for q in response.css("div.quote"):
            # Works just like css selectors, gets every div with class "quote" and each element inside this list a scraper itself

            # ::text is a selector to only get inner HTML
            text = q.css("span.text::text").get()
            author = q.css("small.author::text").get()

            # getall() returns a list of all satisfying elements
            tags = q.css("a.tag::text").getall()

            # Yield like a generator function, to save in json
            # For json file use command scrapy crawl quotes_spider -o quotes.json
            yield {
                "text": text,
                "author": author,
                "tags": tags,
            }

            # To crawl recursively, if we do not know the number of pages before hand
            # attr gives the mentioned attr of the element
            next_page = response.css("li.next a::attr(href)").get()

            if next_page is not None:  # Base condition
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)

            # To save the response in a file
            '''
            with open(filename, "wb") as f:

                f.write(response.body)  # Writing the body as it is in a file

            self.log(f"Saved file as {filename}")
            '''
