#coding:utf8


from example import url_manager, html_downloader, html_outputer, html_parser
class spiderMain(object):

    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def crawl(self, root_url):
        count  = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_next_url():
            try:
                new_url = self.urls.get_new_url()
                print 'crawl %d : %s'%(count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 10:
                    break
                count = count + 1
            except Exception as e:
                print e
                print 'crawl failed'

        self.outputer.output_db()

if __name__ == '__main__':
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = spiderMain()
    obj_spider.crawl(root_url)
