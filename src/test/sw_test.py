import unittest
import nltk
from src.test import sw

class MyTestCase(unittest.TestCase):
    def setUp(self):#alle stopwords herunterladen
        nltk.download('stopwords')#check ob ensprechendes corpus installiert ist

    def tearDown(self):
        print("tearing down")

    def test_first_stopword(self):#definiton von methoden, wird getestet
        self.assertEqual(sw.stopwords() [0], 'i')#testet auf gleichheiten
        #assertEqual ist eine testmethode die testet ob beide
        #übergebene parametr gleich sind. 
    def stopwords(self):
        self.assertEqual(sw.stopwords(), nltk.corpus.stopwords.words('english'))


if __name__ == '__main__':
    unittest.main()


