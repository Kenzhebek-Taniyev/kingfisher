import requests
from bs4 import BeautifulSoup
from Locators.locators import locators
from Parser.parser import Parser


# from Parser.parser import Parser


class AllPages:
    def __init__(self, link):
        page_content = requests.get(link).content
        self.link = link
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def items(self):
        return [Parser(e, self.link) for e in self.soup.select(locators.child)]
