from unittest import TestCase
from HW1 import HW1

class TestHW1(TestCase):
    def test_readFromFileIntoArray(self):
        # Arrange: Create an instance of HW1 and assign to testHW1
        testHW1 = HW1()
        # Act: call the readFromFileIntoArray on testHW1
        testHW1.readFromFileIntoArray("intfile.txt")
        # Assert: check that length of testHW1.OneD is 17 (the number of ints in the file)
        self.assertEqual(len(testHW1.OneD), 17)