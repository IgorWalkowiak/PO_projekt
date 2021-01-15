import product
import unittest

class Test_Product(unittest.TestCase):

    def whenInputOkThenNoException(self):
        prod = product.Product('test', 1, 5)
        self.assertEqual(prod.name, 'test')
        self.assertEqual(prod.amount, 1)
        self.assertEqual(prod.price, 5)

    def whenInputaOkThenNoException(self):
        prod = product.Product('test', 1, 2)
        self.assertEqual(prod.price, 2)


if __name__ == '__main__':
    unittest.main()