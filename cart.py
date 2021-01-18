

class Cart(dict):
    def __init__(self):
        self.content = []
        dict.__init__(self)

    def add(self, prodId, amount):
        for _ in range(int(amount)):
            self.content.append(prodId)

    def getUnique(self):
        unique = list(set(self.content))
        return unique

    def countProduct(self, prodId):
        count = self.content.count(prodId)
        return count
