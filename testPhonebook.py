import unittest
from phonebook import Phonebook

#python3 -m unittest

class PhonebookTest(unittest.TestCase):

    def test_create_phonebook(self):
        phonebook = Phonebook()

    def test_lookup_entry(self):
        phonebook = Phonebook()
        phonebook.add("B", "12")
        self.assertEqual("12", phonebook.lookup("B"))

        
                    
