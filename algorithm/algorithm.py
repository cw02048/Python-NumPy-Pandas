# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 16:37:08 2019

@author: cw020
"""

def match(P, S, n, m):
    
    cnt = 0
    l = -1
    r = 0
    matched = False
    
    while ((l < n - m) and matched == False) or cnt == 0 :
        l = l + 1
        r = 0
        matched = True
        cnt = cnt + 1
        
        print(l, r)
        
        while ((r < m) and matched) or cnt == 1 :
                
                matched = P[r] == S[l + r]
                r = r + 1
                cnt = cnt + 1
                print(matched)
                print(l, r)
    
    if r == m and matched == True :
        print('string의 ' + str(l+1) + '번째부터 입력하신 pattern이 존재합니다.')
        return
        
    else :
        print('문자열 안에 입력하신 문자열이 존재하지않습니다.')
        return
        

def main():
    
    S = input('문자열(S)을 입력하시오: ')
    P = input('문자열(S) 안에서 찾고싶은 패턴(P)을 입력하시오: ')
    
    if 1 <= len(P) <= len(S):
        match(P, S, len(S), len(P))
        
    elif len(P) == 0 or len(S) == 0:
        print('\n값을 모두 입력해주세요.')
        
    elif len(P) > len(S):
        print('\n문자열(S)의 길이보다 찾고싶은 패턴(P)의 길이가 더 큽니다.')
        
main()