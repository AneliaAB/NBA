# Import scrapy
#!pip install scrapy
import scrapy
import time

# Import the CrawlerProcess: for running the spider
from scrapy.crawler import CrawlerProcess

# Create the Spider class
class DC_Chapter_Spider(scrapy.Spider):
  name = "dc_chapter_spider"
  # start_requests method
  def start_requests(self):
    yield scrapy.Request(url = 'https://www.basketball-reference.com/leagues/',
                         callback = self.parse_front)
  # First parsing method
  def parse_front(self, response):
    link_path = response.xpath('//th[@data-stat="season"]/a')
    date_path_ext = link_path.xpath('./text()').extract()
    seasons.append(date_path_ext)
    links_to_follow = link_path.xpath('./@href')
    for url in links_to_follow:
        yield response.follow(url = url,
                            callback = self.parse_results)
        time.sleep(2)

  def parse_results(self, response):
    link_to_follow = response.xpath('//ul[@class="hoversmooth"]/li[3]/a/@href')
    for url in link_to_follow:
        yield response.follow(url = url,
                                callback = self.parse_filter)
    time.sleep(2)
    link_to_follow_list.append(link_to_follow)

  def parse_filter(self, response):
    #header = response.xpath('//h1/span[@class="header_end"]/text()')
    #header_list.append(header)
    filter_path = response.xpath('//div[@class="filter"]//div/a/@href')
    filter_path_list.append(filter_path)
    yield response.follow(url = filter_path,
                            callback = self.parse_table)
    time.sleep(2)
    
  def parse_table(self, response):
    date = response.xpath('//th[@data-stat="date_game"]/a/text()').extract()
    visitor = response.xpath('//td[@data-stat="visitor_team_name"]/a/text()')
    visitor_pts = response.xpath('//td[@data-stat="visitor_pts"]/text()').extract()
    home = response.xpath('//th[@data-stat="home_team_name"]/a/text()').extract()
    home_pts = response.xpath('//td[@data-stat="home_pts"]/text()').extract()
    arena = response.xpath('//td[@data-stat="arena_name"]/text()').extract()
    arena_list.append(arena)
    visitor_list.append(visitor)


    link_to_follow = response.xpath('//td[@data-stat="box_score_text"]/a/@href')
    yield response.follow(url = link_to_follow,
                            callback = self.parse_box_score)

  def parse_box_score(self, response):
    print("Box score")


seasons = []
link_to_follow_list = []
filter_path_list = []
arena_list = []
visitor_list = []

dict_data = dict()

# Run the Spider
process = CrawlerProcess()
process.crawl(DC_Chapter_Spider)
process.start()

print('Try out')
print(seasons[1:5])
print(link_to_follow_list[1:5])
print(arena_list[1:5])
print(filter_path_list[1:5])
print(visitor_list[1:5])