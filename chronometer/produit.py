# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 20:04:52 2026

@author: steev
"""

import random as rd

def generation_nombre():
    
    a = rd.randrange(10**(8),10**(14))
    b = rd.randrange(10**(8),10**(14))
    
    return a*b

if __name__ == "__main__":
    print(generation_nombre())