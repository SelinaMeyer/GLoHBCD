import scrapy

class psychoTherapieSpiderClass(scrapy.Spider):

    name = "PsychoTherapie"

    start_urls = [
        'https://www.adipositas24.de/community/index.php?board/197-psychologische-therapie/&pageNo=1',
    ]

    def parse(self, response):
        pages = int(response.css('nav::attr(data-pages)').get())
        page = 1
        while page <= pages:
            url = "https://www.adipositas24.de/community/index.php?board/197-psychologische-therapie/&pageNo="+str(page)
            page += 1
            yield response.follow(url, self.parse_page)


    def parse_page(self, response):

        threads = response.xpath("//*[(@class = 'wbbThread jsClipboardObject') and (@data-is-link='0')]")

        for thread in threads:

            thread_absolute_link = thread.xpath(".//a[@class = 'messageGroupLink wbbTopicLink']/@href").extract_first()

            yield response.follow(thread_absolute_link, self.parse_thread)



    def parse_thread(self, response):

        with open('./post_ids.txt') as f:
            post_ids = [ int(line.strip()) for line in f ]

        comments = response.xpath("//*[@data-object-type='com.woltlab.wbb.likeablePost']")

        title = response.xpath("//*[@class = 'boxHeadline marginTop wbbThread labeledHeadline']/h1/a/text()").extract_first()
        thread_id = int(response.css('header::attr(data-thread-id)').get())

        for comment in comments:

            post_id = int(comment.css('article::attr(data-post-id)').get())

            if (post_id in post_ids):

                content = "".join(comment.xpath(".//*[@class = 'messageText']/text()").extract())
                content = content.replace("\t", "")
                content = content.replace("\r", "")
                username = "".join(comment.xpath(".//*[@itemprop = 'name']/text()").extract_first())
                date = "".join(comment.xpath(".//*[@class = 'datetime']/text()").extract())

                yield {
                    "title" : title,
                    "thread_id": thread_id,
                    "post_id": post_id,
                    "date" : date,
                    "username" : username,
                    "content" : content,
                }

        next_page = response.xpath("//*[@title='Nächste Seite']/@href").extract_first()

        if (next_page is not None):
            yield response.follow(next_page, self.parse_thread)





