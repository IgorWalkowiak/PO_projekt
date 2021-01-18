"""
Cart is a class to presents user virtual cart in the shop.
There is three methods:

1. **add** - Method add product to cart
2. **getUnique** - Method gives unique products in cart
3. **countProduct** - Method count specific product in cart
"""


class Cart():
    def __init__(self):
        self.content = []

    def add(self, prodId, amount):
        int(prodId)
        for _ in range(int(amount)):
            self.content.append(prodId)

    def getUnique(self):
        unique = list(set(self.content))
        unique.sort()
        return unique

    def countProduct(self, prodId):
        count = self.content.count(prodId)
        return count
