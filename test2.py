# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:22:20 2019

@author: cw020
"""


def main():
    n = int(input())
    w = input()
    i = 0
    
    while i <= n // 2:
        
        if i < n//2:
            
            if w[i] == w[n-1-i]:
                i += 1
                
            else:
                print("NO")
                return
        elif i <= n //2:
            
            w_list2 = []
            
            while i + 1 < n:
                
                w_list2.extend(w.split(w[n//2:i+1]))
                w_list2.remove('')  
                
                if w[0:n//2] in w_list2:
                    print("YES")
                    print(w[n//2:i+1])
                elif w[i+1:] in w_list2:
                    print("YES")
                    print(w[n//2:i+1])
                elif i + 1 == n-1:
                    print("NO")
    
                i += 1

    return
        
    
    
    
main()