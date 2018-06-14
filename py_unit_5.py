#py_unit_5.py

import unittest

def adder(a, b):
    return a + b

class TestMe(unittest.TestCase):
    def test_1(self):
        obj = [(2, 2, 4),
               (4, 4, 8),
               [(1 + 7j), (2 + 8j), (3 + 15j)]
              ]  
        for addent1, addent2, expected in obj: 
            msg = "Yo, dude, we're not adding {} and {} right!"
            self.assertEqual(expected, adder(addent1, addent2), msg.format(addent1, addent2))
                                            

if __name__ == '__main__':
    unittest.main()