from trigrams import slice_book
from trigrams import book_dict
from trigrams import main
import unittest

class testIt(unittest.TestCase):
	def test_1(self):
		self.assertEqual(slice_book('test.txt'), ["this", "is", "a", "test"])
	
	def test_2(self):
		self.assertEqual(book_dict(['the', 'the', 'this']), {'the the': ['the','this']} )
		
if __name__ == '__main__':
	unittest.main()
		
		
