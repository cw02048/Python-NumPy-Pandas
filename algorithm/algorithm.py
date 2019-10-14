# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 16:37:08 2019

@author: cw020
"""

def match(P, S, n, m):
    
    cnt = 0 # 파이썬에 do while문이 없어서 cnt로 첫 실행은 무조건 되게 설정
    l = -1 # 현재 검사 중인 문자의 패턴 시작 위치 (S기준)
    r = 0 # 현재 검사 중인 문자의 l로부터의 위치
    matched = False
    
    # 패턴을 찾거나, 패턴의 시작 위치가 문자열의 길이 - 패턴의 길이와 같아지면 반복문 종료 (돌려봤자 어차피 길이가 안되기 때문) 
    while ((l < n - m) and matched == False) or cnt == 0 :
        l = l + 1
        r = 0
        matched = True
        cnt = cnt + 1
        
        # 패턴이 맞지 않거나, 패턴을 찾으면 반복문 종료
        while ((r < m) and matched) or cnt == 1 :
                
                matched = P[r] == S[l + r] # 문자열의 매칭 여부 확인
                r = r + 1
                cnt = cnt + 1
    
    # 마지막에 매칭한 위치인 r과 패턴의 길이가 같고, 마지막 매칭이 True이면 패턴 존재
    if r == m and matched == True :
        print('\nstring의 ' + str(l+1) + '번째부터 입력하신 pattern이 존재합니다.')
        return
    
    # 만약 아니면
    else :
        print('\n문자열 안에 입력하신 문자열이 존재하지않습니다.')
        return
        
def main():
    
    S = input('문자열(S)을 입력하시오: ')
    P = input('문자열(S) 안에서 찾고싶은 패턴(P)을 입력하시오: ')
    
    # 패턴의 길이는 1보다 크거나 같아야하고, 문자열보다 작거나 같아야함
    if 1 <= len(P) <= len(S):
        match(P, S, len(S), len(P))
    
    # 패턴의 길이나 문자열의 길이를 입력 안했을 때
    elif len(P) == 0 or len(S) == 0:
        print('\n값을 모두 입력해주세요.')
        
    # 패턴의 길이가 문자열의 길이보다 클 때
    elif len(P) > len(S):
        print('\n문자열(S)의 길이보다 찾고싶은 패턴(P)의 길이가 더 큽니다.')
        
main()