from unittest import TestCase, main

from codewars.katas.kyu_8.abbreviate_a_two_word_name import abbrevName

class Teste_abbreviate_a_two_word_name(TestCase):
    def teste_abbreviate_a_two_word_name(self):

        self.assertEquals(abbrevName("Sam Harris"), "S.H");
        self.assertEquals(abbrevName("Patrick Feenan"), "P.F");
        self.assertEquals(abbrevName("Evan Cole"), "E.C");
        self.assertEquals(abbrevName("P Favuzzi"), "P.F");
        self.assertEquals(abbrevName("David Mendieta"), "D.M");

if __name__ == '__main__':
    main()
