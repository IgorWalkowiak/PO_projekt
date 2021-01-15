

class Product:
    def __init__(self, name, amount, price):
        self.name = name

        if not float(amount).is_integer() and float(amount) < 0:
            raise ValueError
        else:
            self.amount = amount

        if float(price) < 0.0:
            raise ValueError
        else:
            self.price = price
