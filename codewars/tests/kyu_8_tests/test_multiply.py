from unittest import TestCase, main

from codewars.katas.kyu_8.multiply import multiply

class Teste_multiply(TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(2,2), 4)

if __name__ == '__main__':
    main()
