from unittest import TestCase, main

from codewars.katas.kyu_8.dna_to_rna_conversion import DNAtoRNA

class Teste_DNAtoRNA(TestCase):
    def teste_DNAtoRNA(self):

        self.assertEqual(DNAtoRNA("TTTT"), "UUUU")
        self.assertEqual(DNAtoRNA("GCAT"), "GCAU")
        self.assertEqual(DNAtoRNA("GACCGCCGCC"), "GACCGCCGCC")

if __name__ == '__main__':
    main()
