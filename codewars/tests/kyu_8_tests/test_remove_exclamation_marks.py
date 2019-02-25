from unittest import TestCase, main

from codewars.katas.kyu_8.remove_exclamation_marks import remove_exclamation_marks

class Teste_remove_exclamation_marks(TestCase):
    def teste_remove_exclamation_marks(self):
        self.assertEqual(remove_exclamation_marks("Hello World!"), "Hello World")
        self.assertEqual(remove_exclamation_marks("Hello World!!!"), "Hello World")
        self.assertEqual(remove_exclamation_marks("Hi! Hello!"), "Hi Hello")
        self.assertEqual(remove_exclamation_marks(""), "")
        self.assertEqual(remove_exclamation_marks("Oh, no!!!"), "Oh, no")

if __name__ == '__main__':
    main()
