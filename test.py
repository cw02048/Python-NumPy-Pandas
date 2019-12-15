# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 11:15:00 2019

@author: cw020
"""


def main():
    
    n1, n2, n3 = map(int, input().split())
    i = 0
    n = n1 + n2 + n3
    n_dic = {}
    n_list = []
    while i < n:
        num = input()
        if num in n_dic:
            n_dic[num] += 1
        else:
            n_dic[num] = 1
        i += 1
    for i in n_dic.keys():
        if n_dic[i] > 1:
            n_list.append(i)
    n_list.sort()
    print()
    print(len(n_list))
    for i in n_list: 
        print(int(i))
        
main()