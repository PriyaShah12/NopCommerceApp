import unittest

class LoginTest(unittest.TestCase):
    def test_loginByGmail(self):
        print("This is login by gmail")
        self.assertTrue(True)

    def test_loginByFacebook(self):
        print("This is login by facebook")
        self.assertTrue(True)

    def test_loginByTwitter(self):
        print("This is login by twitter")
        self.assertTrue(True)


if __name__ =="__main__":
    unittest.main()