# -*- coding: utf-8 -*-
"""
Created on Sun May 22 01:17:49 2022

@author: muhammad bilal
"""

import pdb

def sum_values(a, b):
    return a + b

def test_function():
    pdb.set_trace()  #we have added a breakpoint here. The code pause execution here.
    print('This is the first line')
    print("This is the second line.")
    value  = sum_values(2, 3)
    print('The code is done!')
    return value 


test_function()