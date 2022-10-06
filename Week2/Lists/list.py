# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 09:07:53 2021

@author: jcdav

Lists
"""

list = [4,'jaxx', 8,'jordi', 45, 'diana', 'bear']

#function with if statement to read the list

def who_is_there(list):
    if 'jaxx' in list:
        print("Hello, Jaxx.")
        print("Super smart kid!")
        
    if 'jordi' in list:
        print("Hello, Jordi.")
        print("Amazing kid!")
        
    if 'julio' in list:
        print("Hello, Julio.")
        print("Great dad!")
        
    if 'diana' in list:
        print("Hello, Diana.")
        print("Worlds best mom!")
        
    if 'bear' in list:
        print("ROOOAAARR.... ROOOOAAAARRRR!")
        print("Cranky BEARRRRRR!")
    
    print(list.sort(-1))
    
    
