from cart import Cart
import unittest

PROD_ID_1 = '1'
PROD_ID_2 = '2'
PROD_ID_WRONG = 'a2'
PROD_ID_3 = '3'

class TestCart(unittest.TestCase):
    def test_when_cart_init_call_Then_no_exception(self):
        cart = Cart()

    def test_when_empty_cart_then_count_eq_0(self):
        cart = Cart()
        self.assertEqual(cart.countProduct(PROD_ID_1), 0)
        self.assertEqual(cart.countProduct(PROD_ID_2), 0)
        self.assertEqual(cart.countProduct(PROD_ID_3), 0)

    def test_when_add_to_cart_Then_countProuct_OK(self):
        cart = Cart()
        cart.add(PROD_ID_1, 1)
        self.assertEqual(cart.countProduct(PROD_ID_1), 1)

    def test_when_wrong_add_to_cart_Then_exception(self):
        cart = Cart()
        with self.assertRaises(ValueError):
            cart.add(PROD_ID_WRONG, 1)

    def test_when_add_to_cart_Then_many_countProuct_OK(self):
        cart = Cart()
        cart.add(PROD_ID_1, 3)
        self.assertEqual(cart.countProduct(PROD_ID_1), 3)

        cart.add(PROD_ID_2, 8)
        self.assertEqual(cart.countProduct(PROD_ID_2), 8)

        cart.add(PROD_ID_3, 9)
        self.assertEqual(cart.countProduct(PROD_ID_3), 9)

    def test_when_add_to_cart_one_prod_Then_countProuct_OK(self):
        cart = Cart()
        cart.add(PROD_ID_1, 3)
        self.assertEqual(cart.countProduct(PROD_ID_1), 3)

        cart.add(PROD_ID_1, 8)
        self.assertEqual(cart.countProduct(PROD_ID_1), 11)

        cart.add(PROD_ID_1, 9)
        self.assertEqual(cart.countProduct(PROD_ID_1), 20)

    def test_when_empty_cart_Then_getUnique_empty(self):
        cart = Cart()
        self.assertEqual(cart.getUnique(), [])

    def test_when_cart_not_empty_Then_getUnique_OK(self):
        cart = Cart()
        cart.add(PROD_ID_1, 1)
        cart.add(PROD_ID_2, 1)
        cart.add(PROD_ID_2, 1)
        self.assertEqual(cart.getUnique(), [PROD_ID_1,PROD_ID_2])


if __name__ == '__main__':
    unittest.main()