#solution_python2_chapter02_unttest.py
import unittest

from solution_python2_chapter02_tested import add_numbers
from solution_python2_chapter02_tested import NoneTypeError
from solution_python2_chapter02_tested import WrongDataTypeError

class TestSuite(unittest.TestCase):
    def test_addition_success(self):
        "these are expected to pass"
        things_to_test={'int': 3, 'float:':5.0, 
                        'complex':(1+3j), 'dict':{'a':1, 'b':2}, 
                        'list':[1,2,3], "None":None}
        
        #things to test (input1, input2, expected)
        things_to_test=( (3,3,6),
                         (3.0, 3.0, 6.0),
                         ( (2+2j), (3+3j), (5+5j) ),
                         ( [1,2,3], [1,2,3], [1,2,3,1,2,3] ),
                        )
        
        #parsing tuple in header of for
        msg="Sorry dude.  {} + {} should be {}, but you got {}"
        for first, second, expected in things_to_test:
            answer=add_numbers(first,second)
            self.assertEqual(answer, 
                             expected, 
                             msg=msg.format(first, second, 
                                               expected, answer))
           
    def test_addition_raise_WrongDataType(self):
        "check that WrongDataTypeError is raised"
        things_to_test=( ( {'a':1, 'b':2} , {'a':1, 'b':2} ),
                       )
        for thing in things_to_test:
            first, second = thing
            self.assertRaises(WrongDataTypeError, add_numbers, first, second)
        
     
    def test_addition_raise_NoneType(self):
        "check that NoneTypeError raised"
        things_to_test=((None, None),
                        (None, 2),
                        (2, None)
                        )
        for first, second in things_to_test:
            self.assertRaises(NoneTypeError, add_numbers, first, second)        
        pass
            
if __name__=='__main__':
    unittest.main()
