from collections import OrderedDict
import re

numberItems = input()

itemsBought = OrderedDict()

for items in range(int(numberItems)):
    itemPrice = input()
    regexObj = re.search(r'(\D+)(\d+)', itemPrice)
    item = regexObj.group(1).strip()
    price = regexObj.group(2)
    if item not in itemsBought:
        itemsBought[item] = int(price)
    else:
        itemsBought[item] += int(price)

[print(key, value) for key, value in itemsBought.items()]