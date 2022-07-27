# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: muhammad bilal

This is a temporary script file.
"""

import unittest 

def join_names(first, last):
    return ' '.join([first.capitalize(), last.capitalize()])


return_data =  join_names('ahmed', 'hadi')
print(return_data)


class TestStringMethods(unittest.TestCase):
    def test_is_capitalized(self):
        temp1, temp2 = return_data.split(' ')
        self.assertTrue(temp1.istitle())
        self.assertTrue(temp2.istitle())
    
    def test_length(self):
        self.assertTrue(len(return_data.split(' ')), 2)
    
    def test_split(self):
        self.assertEqual(type(return_data), str)

if __name__ == '__main__':
    unittest.main()