from unittest import TestCase, main

from codewars.katas.kyu_8.sum_of_positive import positive_sum

class Teste_positive_sum(TestCase):
    def teste_positive_sum(self):

        self.assertEqual(positive_sum([1,2,3,4,5]),15)
        self.assertEqual(positive_sum([1,-2,3,4,5]),13)
        self.assertEqual(positive_sum([-1,2,3,4,-5]),9)

        self.assertEqual(positive_sum([]),0)

        self.assertEqual(positive_sum([-1,-2,-3,-4,-5]),0)
        self.assertEqual(positive_sum([2,2]), 4)

if __name__ == '__main__':
    main()
