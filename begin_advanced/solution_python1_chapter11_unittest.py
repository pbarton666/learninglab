#py_basic_unittest_2.py

from py_screener import screener

def odd_man_out(inp):
    """If input looks like an odd integer, return
        twice its value; otherwise, return None"""

    try: #If it's a number, can it be cast as an integer?
        inp = int(inp)
    except:
        return None
    #try: #Is it a number at all?  If not, give up.
        #inp/1
    #except:
        #return None

    #If it's a number, is it odd?
    if inp % 2:  #returns 0 if even
        return(inp*2)

if __name__=='__main__':
    import unittest
    class tester(unittest.TestCase):
        def test_odd_integer(self):
            self.assertEqual(odd_man_out(3), 6)
        def test_even_integer(self):
            self.assertEqual(odd_man_out(4), None)
        def test_odd_string(self):
            self.assertEqual(odd_man_out('123'), 246)
        def test_odd_float(self):
            self.assertEqual(odd_man_out(31.0), 62.0)
        def test_list(self):
            self.assertEqual(odd_man_out([1,2,3]), None)					
        def test_complex(self):
            self.assertEqual(odd_man_out(complex(1,2)), None)
    unittest.main()