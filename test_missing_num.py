#import test library
import unittest
from missing_num import missing_numbers

class TestMissingNum(unittest.TestCase):
    def test_missing_number(self):
        missing_result = [4, 8]
        self.assertEqual(missing_numbers([1, 2, 3, 5, 6, 7,9]), missing_result)
        
if __name__ == "__main__":
    unittest.main()