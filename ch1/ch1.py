# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 12:05:59 2023

@author: user1
"""
from os import getcwd
num=input('Enter integer number : ')
try:
    if isinstance(int(num),int):
        print(int(num)*2)
    else:
        print('Error')
except ValueError:
    print('Error:Plz only insert integer Number')


