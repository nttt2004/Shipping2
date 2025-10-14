import unittest
from shipping import calculate_shipping_fee  

class TestShippingFeeC2(unittest.TestCase):
    def test_case_1(self):
        result = calculate_shipping_fee(52, 1396)
        self.assertEqual(result, 0)

    def test_case_2(self):
        result = calculate_shipping_fee(42, 2000)
        expected = 20000 + 630000 + 100000
        self.assertEqual(result, expected)

    def test_case_3(self):
        result = calculate_shipping_fee(3, 72)
        expected = 20000 + 15000 + 7200
        self.assertEqual(result, expected)

    def test_case_4(self):
        result = calculate_shipping_fee(17, 465)
        expected = 20000 + 170000 + 37200
        self.assertEqual(result, expected)

    def test_case_5(self):
        result = calculate_shipping_fee(18, 84)
        expected = 20000 + 180000 + 8400
        self.assertEqual(result, expected)

    def test_case_6(self):
        result = calculate_shipping_fee(39, 92)
        expected = 20000 + 585000 + 9200
        self.assertEqual(result, expected)

    def test_case_7(self):
        result = calculate_shipping_fee(42, 687)
        expected = 20000 + 630000 + 34350
        self.assertEqual(result, expected)

# if __name__ == '__main__':
#     unittest.main()
