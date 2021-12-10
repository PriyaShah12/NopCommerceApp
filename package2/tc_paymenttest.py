import unittest

class paymentTest(unittest.TestCase):
    def test_paymentInDollar(self):
        print("Payment in Dollar ")
        self.assertTrue(True)

    def test_paymentInRupee(self):
        print("Payment in Rupee ")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()