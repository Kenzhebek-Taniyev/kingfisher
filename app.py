from utils import database
from Locators.types import types
from Pages.allPages import AllPages

all_goods = []

for link in types.product_to_name.values():
    print(link)
    items = AllPages(link).items
    all_goods.extend(items)

    # data can be added to database directly from here (so next lines will be unnecessary)
    # for item in items:
    #     database.addOne(item.category, item.name, item.city, item.price)


with open("data.txt", "a",  encoding="utf-8") as f:
    for i in all_goods:
        f.write(f'{i.category}:#: {i.name}:#: {i.city}:#: {i.price}\n')
        # data can be added directly from here
        # database.addOne(i.category, i.name, i.city, i.price)


database.createDatabase()
database.updateAll('data.txt')
database.seeAll()
