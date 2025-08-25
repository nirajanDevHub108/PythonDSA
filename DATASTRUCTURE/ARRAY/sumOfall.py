def sum_till_n(n: int) -> int:
    """Return sum of numbers from 1 to n."""
    if n < 0:
        raise ValueError("n must be non-negative")
    return n * (n + 1) // 2


# -------- TEST CASES --------
import unittest

class TestSumTillN(unittest.TestCase):

    def test_small_numbers(self):
        self.assertEqual(sum_till_n(2), 3)   # 1+2 =3 
        self.assertEqual(sum_till_n(1), 1)   # sum = 1
        self.assertEqual(sum_till_n(5), 15)  # 1+2+3+4+5 = 15

    def test_large_number(self):
        self.assertEqual(sum_till_n(100), 5050)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            sum_till_n(-5)


if __name__ == "__main__":
    unittest.main()