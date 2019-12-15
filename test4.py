# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 19:19:18 2019

@author: cw020
"""

def main():
    
    n_list = []
    n = int(input())
    i = 0
    
    while i < n:
        
        tmp = input()
        
        n_list.append(tmp[0:len(tmp)-3])
        
        i += 1
        
    for n in sorted(n_list):
            
            print(n)
            

main()