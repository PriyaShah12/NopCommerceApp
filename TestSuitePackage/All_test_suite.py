import unittest

from package1.tc_login import LoginTest
from package1.tc_signIn import SignInTest
from package2.tc_paymenttest import paymentTest
from package2.tc_paymentreturn import PaymentReturnTest

tc1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2=unittest.TestLoader().loadTestsFromTestCase(SignInTest)
tc3=unittest.TestLoader().loadTestsFromTestCase(paymentTest)
tc4=unittest.TestLoader().loadTestsFromTestCase(PaymentReturnTest)


sanityTestSuite=unittest.TestSuite([tc1,tc2])
functionalTestSuite=unittest.TestSuite([tc3,tc4])
masterTestSuite=unittest.TestSuite([tc1,tc2,tc3,tc4])

unittest.TextTestRunner().run(masterTestSuite)