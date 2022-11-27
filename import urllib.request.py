#A web scraper with Python that pulls all the stories from Google News by extracting all the tags from the HTML of Google News


import urllib.request       #Python has a built-in module, named urllib, for working with URLs.
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):   #The __init__ method uses a website to extract as a parameter
        self.site = site
        
    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
    
    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html,parser)
    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html,parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "articles" in url:
                print("\n" + url)
                
news = "https://news.google.com/"
Scraper(news).scrape()