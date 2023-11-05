import unittest
import logging

from program01_ita import decode_digits

# Get logger
logger = logging.getLogger('program01.ita')
logger.setLevel(logging.INFO)

class Test(unittest.TestCase):
    
    def test_import_decide_digits(self):

        result = decode_digits([1, 1, 1], [10, 10, 10])
        self.assertEqual(result, 111)

        result = decode_digits([1, 1, 1], [2, 2, 2])
        self.assertEqual(result, 7)

        result = decode_digits([1, 1, 1], [2, 4, 10])
        self.assertEqual(result, 105)

if __name__ == '__main__':
    unittest.main()
