from dataclasses import dataclass
from bs4 import BeautifulSoup
import urllib
from time import sleep

NYNCB_GK_URL = "http://www.moa.gov.cn/gk/"

@dataclass
class Crawler():
    url : str = ''
    # def __init__(self, url):
    #     self.url = url
    # def __post__init(self):
    #     print(f'post:{self.url}')
    #     self.response = urllib.request.urlopen(self.url)
    #     # self.response = urllib.url

    def crawl(self):
        print(self.url)
        self.response = urllib.request.urlopen(self.url)
        self.soup = BeautifulSoup(self.response, 'html.parser')
        print(self.soup.title.string)
        print(self.soup.find_all('a'))


def main():
    nyncb_crawler = Crawler(NYNCB_GK_URL)
    count = 0
    while True:
        count += 1
        print(f'crawl {count}')
        nyncb_crawler.crawl()
        sleep(3)


main()
