# %%writefile test_mutation.py
import unittest
from shipping import calculate_shipping_fee

class TestShippingFee(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(calculate_shipping_fee(25, 1000), 445000)

    def test_case2(self):
        self.assertEqual(calculate_shipping_fee(25, 0), 395000)

    def test_case3(self):
        self.assertEqual(calculate_shipping_fee(25, 100), 403000)

    def test_case4(self):
        self.assertEqual(calculate_shipping_fee(25, 500), 420000)

    def test_case5(self):
        self.assertEqual(calculate_shipping_fee(25, 2000), 495000)

    def test_case6(self):
        self.assertEqual(calculate_shipping_fee(0, 1000), 70000)

    def test_case7(self):
        self.assertEqual(calculate_shipping_fee(5, 1000), 120000)

    def test_case8(self):
        self.assertEqual(calculate_shipping_fee(20, 1000), 370000)

    def test_case9(self):
        self.assertEqual(calculate_shipping_fee(50, 1000), 820000)

    def test_case10(self):
        self.assertEqual(calculate_shipping_fee(-14, 1392), 0)

    def test_case11(self):
        self.assertEqual(calculate_shipping_fee(2, 38), 33800)

    def test_case12(self):
        self.assertEqual(calculate_shipping_fee(3, 372), 64760)

    def test_case13(self):
        self.assertEqual(calculate_shipping_fee(4, 1476), 113800)

    def test_case14(self):
        self.assertEqual(calculate_shipping_fee(13, 73), 157300)

    def test_case15(self):
        self.assertEqual(calculate_shipping_fee(18, 216), 217280)

    def test_case16(self):
        self.assertEqual(calculate_shipping_fee(7, 673), 123650)

    def test_case17(self):
        self.assertEqual(calculate_shipping_fee(28, 64), 446400)

    def test_case18(self):
        self.assertEqual(calculate_shipping_fee(42, 432), 684560)

    def test_case19(self):
        self.assertEqual(calculate_shipping_fee(38, 873), 633650)

# & "C:\Users\Thu Trang\Downloads\Shipping2\mutenv\Scripts\python.exe" "C:\Users\Thu Trang\Downloads\Shipping2\mutenv\Scripts\mut.py" --target shipping --unit-test test_mutation -m --report-html report_html
