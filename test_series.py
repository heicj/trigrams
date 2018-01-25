from trigrams import slice_book
from trigrams import main
import unittest

class testIt(unittest.TestCase):
	def test_1(self):
		self.assertEqual(slice_book("this is a test", ["this", "is", "a", "test"])
		
if __name__ == '__main__':
	unittest.main()
		
		
