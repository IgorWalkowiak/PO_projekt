import product
import unittest

class TestProduct(unittest.TestCase):

    def test_whenInputOkThenNoException(self):
        prod = product.Product('test', 1.0, 5.0)
        self.assertEqual(prod.name, 'test')
        self.assertEqual(prod.amount, 1.0)
        self.assertEqual(prod.price, 5.0)

    def test_when_input_ok_then_no_exception(self):
        prod = product.Product('test', 1.0, 2.0)
        self.assertEqual(prod.price, 2.0)


if __name__ == '__main__':
    unittest.main()
