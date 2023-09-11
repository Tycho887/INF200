# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 16:05:25 2023

@author: Michael
"""

import numpy as np
import csv

def prime_check(n,known):
    for i in known:
        if n%i==0:
            return False
    return True

def write_primes(n):   
    width = 25 # numbers per line
    
    primes = [2]
    for i in range(2,n):
        if prime_check(i, primes):
            primes.append(i)
    length = int(np.ceil(len(primes)/width))
    
    primes = np.array(primes)
    primes.reshape((length,width))
    
    return(primes)
    with open("data/primes.csv", "w") as file_out:
        pass

A = write_primes(1000)

#print(get_primes(1000000))