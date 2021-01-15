import product
import unittest

class TestProduct(unittest.TestCase):

    def test_when_input_ok_then_no_exception(self):
        prod = product.Product('test', 1, 5.0)
        self.assertEqual(prod.name, 'test')
        self.assertEqual(prod.amount, 1)
        self.assertEqual(prod.price, 5.0)

    def test_when_amount_negative_then_exception(self):
        with self.assertRaises(ValueError):
            prod = product.Product('test', -1, 5.0)

    def test_when_amount_not_int_then_exception(self):
        with self.assertRaises(ValueError):
            prod = product.Product('test', 1.5, 5.0)

    def test_when_price_negative_then_exception(self):
        with self.assertRaises(ValueError):
            prod = product.Product('test', 1, -5.0)

    def test_getValue(self):
        prod = product.Product('test', 1, 5.0)
        self.assertEqual(prod.getValue(), 5.0)

        prod = product.Product('test', 3, 2.0)
        self.assertEqual(prod.getValue(), 6)

        prod = product.Product('test', 5, 10)
        self.assertEqual(prod.getValue(), 50)


if __name__ == '__main__':
    unittest.main()
