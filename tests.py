import unittest

from executable import sort

class PackageTests(unittest.TestCase):
    def test_standard_package(self):
            self.assertEqual(sort(1, 1, 1, 1), "STANDARD")

    def test_special_package_bulky(self):
            self.assertEqual(sort(1000, 1000, 1000, 5), "SPECIAL")

    def test_rejected_heavy(self):
            self.assertEqual(sort(10, 10, 10, 100), "SPECIAL")             

    def test_rejected_package(self):
            self.assertEqual(sort(10000, 100000, 10000, 10000), "REJECTED")

    def test_value_zero_error(self):
        self.assertEqual(sort(0,0,0,0), "ERROR: ZERO OR NEGATIVE VALUE")

    def test_value_negative_error(self):
        self.assertEqual(sort(-10,-10,0,0), "ERROR: ZERO OR NEGATIVE VALUE") 

    def test_string_error(self):
        self.assertEqual(sort("a",3,3,3), "ERROR: ONE OR MORE VALUES IS NON NUMERICAL")               

    def test_missing_value_error(self):
        self.assertEqual(sort(None, None, None, None), "ERROR: ONE OR MORE VALUES DOES NOT EXIST")     

if __name__ == '__main__':
    unittest.main()