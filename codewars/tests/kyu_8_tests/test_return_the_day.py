from unittest import TestCase, main

from codewars.katas.kyu_8.return_the_day import whatday

class Teste_return_the_day(TestCase):
    def teste_return_the_day(self):
        self.assertEquals(whatday(1), 'Sunday')
        self.assertEquals(whatday(2), 'Monday')
        self.assertEquals(whatday(3), 'Tuesday')
        self.assertEquals(whatday(8), 'Wrong, please enter a number between 1 and 7')
        self.assertEquals(whatday(20), 'Wrong, please enter a number between 1 and 7')

if __name__ == '__main__':
    main()
