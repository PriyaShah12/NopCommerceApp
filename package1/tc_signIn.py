import unittest

class SignInTest(unittest.TestCase):
    def test_signInByGmail(self):
        print("This is signin  by gmail")
        self.assertTrue(True)

    def test_SignInByFacebook(self):
        print("This is signIn by facebook")
        self.assertTrue(True)

    def test_SignInByTwitter(self):
        print("This is signIn by Twitter")
        self.assertTrue(True)


if __name__ =="__main__":
    unittest.main()