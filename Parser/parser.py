import re
from bs4 import BeautifulSoup
from Locators.types import types
from Locators.locators import locators


class Parser:
    def __init__(self, parent, link):
        self.parent = parent
        self.link = link

    def __repr__(self):
        return f'<{self.category}: {self.name} ({self.price} T ) ({self.city})>'

    @property
    def name(self):
        if self.parent.select_one(locators.NAME) == None:
            return ''
        item = self.parent.select_one(locators.NAME).string
        return item


    @property
    def price(self):
        if self.parent.select_one(locators.PRICE) == None:
            return ''
        item_price = self.parent.select_one(locators.PRICE).string
        pattern = '([0-9 ]+) Т'
        matcher = re.search(pattern, item_price)
        return int(matcher.group(1).replace(" ", ""))


    @property
    def category(self):
        return types.link_to_product[self.link]


    @property
    def city(self):
        return 'No city'
        # if self.parent.select_one(locators.CITY) == None:
        #     return ''
        # return self.parent.select_one(locators.CITY).string


    # @property
    # def href(self):
    #     item = self.parent.select_one(locators.NAME)
    #     if hasattr(item, 'href'):
    #         href = item['href']
    #         return href
    #     else:
    #         return ''