import application
import unittest

class Test_application(unittest.TestCase):


    def test_suma(self):
        self.assertEqual(application.suma([2, 2]), 4)

    def test_resta(self):
        self.assertEqual(application.resta([2, 2]), 0)

    def test_multiply(self):
        self.assertEqual(application.multiply([3,3]),9)

    def test_divide(self):
        self.assertEqual(application.divide([6,3]),2)


if __name__ == '__main__':
    unittest.main()

