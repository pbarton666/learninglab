# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 19:46:54 2017

@author: Kirby Urner


MagicMock is a subclass of Mock with 
all the magic methods pre-created and 
ready to use
"""

from unittest.mock import MagicMock

# arrange
obj = MagicMock(name='Demo')

# act
def gauntlet(m):
    m[1] = 10        # __setitem__(1, 10)
    m('eating arg')  # make it eat

gauntlet(obj)
    
# assert
obj.__setitem__.assert_called_with(1, 10)
obj.assert_called_once_with('eating arg')

print("Called?:", obj.called)
print("# Calls:", obj.call_count)
print("Calls  :", obj.mock_calls)

obj.method.return_value = 42
print("obj.method():", obj.method())

obj.method1.side_effect = ValueError
try:
    obj.method1()
except ValueError:
    print("obj.method1() raised ValueError")