import unittest
from classify_produce import classifyProduce


class TestClassifyProduce(unittest.TestCase):
    def test_boundary_cases(self):
        self.assertEqual(classifyProduce(5, 5, 0), "Average")
        self.assertEqual(classifyProduce(5, 5, 10), "Average")
        self.assertEqual(classifyProduce(5, 5, 30), "Bad")
        self.assertEqual(classifyProduce(0, 5, 15), "Bad")
        self.assertEqual(classifyProduce(5, 5, 15), "Bad")
        self.assertEqual(classifyProduce(10, 5, 15), "Bad")
        self.assertEqual(classifyProduce(5, 0, 0), "Average")
        self.assertEqual(classifyProduce(5, 7, 10), "Good")
        self.assertEqual(classifyProduce(5, 10, 30), "Average")
        self.assertEqual(classifyProduce(5, 5, 15), "Bad")

    def test_equivalence_partitioning(self):
        self.assertEqual(classifyProduce(-13, 3, 7), "Invalid Input")
        self.assertEqual(classifyProduce(8, 9, 1), "Good")
        self.assertEqual(classifyProduce(7, 8, 21), "Average")
        self.assertEqual(classifyProduce(3, 9, 13), "Bad")


if __name__ == "__main__":
    unittest.main()
