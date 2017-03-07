# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12, 2016

@author: Kirby Urner

Typically the unit tests go in a separate file.
Testers could be a different team than developers.
Testers do not need to touch developer code.
"""

import unittest  # <-- the source of assertEqual, etc.

from animal_world import Duck

class AnimalTests(unittest.TestCase):

    def test_OK_name(self):
        """
        Shouldn't be a problem
        """
        daffy = Duck("Daffy")
        self.assertEqual(daffy.name, "Daffy")

    def test_wrong_name(self):
        """
        We expect a ValueError given 'Doggy'
        """
        self.assertRaises(ValueError, Duck, "Doggy")
    
if __name__ == "__main__":
    unittest.main()

