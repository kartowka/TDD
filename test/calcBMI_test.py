import unittest
from src.calcBMI import BMI

class bmitest(unittest.TestCase):
    def test_bubbleSort(self):
        # stub
        list1=[9,8,7,6,5,4,3,2,1]

        # assume

        list1sorted=[1,2,3,4,5,6,7,8,9]

        # action

        result1=BMI.bubble_sort(list1)

        # expect/assert

        self.assertEqual(result1,list1sorted)


if __name__=='__main__':
    unittest.main()