import unittest
import cap

class TestCap(unittest.TestCase):

	def test_one_word(self):
		text = "gustavo"
		result = cap.cap_text(text)
		self.assertEqual(result,"Gustavo")

	def test_multiple_words(self):
		text = "gustavo lage"
		result = cap.cap_text(text)
		self.assertEqual(result,"Gustavo Lage")

if __name__ == '__main__':
	unittest.main()