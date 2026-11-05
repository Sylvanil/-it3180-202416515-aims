import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        for i in range(20):
            self.assertTrue(cart.add_dvd(DigitalVideoDisc(f"DVD {i}", cost=10.0)))
        self.assertFalse(cart.add_dvd(DigitalVideoDisc("DVD 21", cost=10.0)))

    def test_total_cost_with_discount(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("DVD 1", cost=100.0))
        self.assertAlmostEqual(cart.total_cost_with_discount(20), 80.0)

    def test_total_cost_with_invalid_discount(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("DVD 1", cost=100.0))
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(-10)


if __name__ == "__main__":
    unittest.main()

    def test_sort_cart(self):
        cart = Cart()
        d1 = DigitalVideoDisc("Zorro", cost=10.0)
        d2 = DigitalVideoDisc("Alpha", cost=30.0)
        cart.add_dvd(d1)
        cart.add_dvd(d2)
        cart.sort_by_title()
        self.assertEqual(cart.lsDVD[0].title, "Alpha")
        cart.sort_by_cost()
        self.assertEqual(cart.lsDVD[0].cost, 30.0)
