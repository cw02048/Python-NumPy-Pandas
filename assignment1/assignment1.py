# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# 정수 입력받는 함수
def inputNum():
    
    # stop이나 정수를 받을 때까지 반복
    while True:
        num = input('Enter an unsigned integer: ')
        
        # stop을 입력받으면 stop을 리턴해줌
        if(num == 'stop'):
            print('\nThank you for using this program')
            return 'stop'
        
        # 입력받은 것이 숫자인지 확인
        elif(num.isdigit() == True):
            
            # 숫자가 양의 정수이면 그 수를 리턴
            num = float(num)
        
            if (num % 1 == 0 and num > 0):
                return int(num)
            
# 변환할 진수를 입력받는 함수
def choice():
    
    # 올바른 진수 명령어를 입력받을 때까지 반복
    while True:
        choice = input('b or B for binary, o or O for octal, h or H for hexadecimal: ')
        
        # 2진수
        if(choice == 'b' or choice == 'B'):
            return 2
        # 8진수
        elif(choice == 'o' or choice == 'O'):
            return 8
        # 16진수
        elif(choice == 'h' or choice == 'H'):
            return 16
        # 올바르지 않은 명령어 입력시
        else:
            print('Invalid choice!')
        
# 진수 변환을 계산해주는 함수
def calculate(num, cmd): # num은 진수로 나누어줄 수, cmd는 변환할 진수
    
    numList = [] # 나눈 나머지들이 순서대로 들어가는 리스트
    insList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'] # 진수 변환 코드를 줄이기 위해 꺼내쓰기용 리스트
    res = '' # 리스트를 문자열로 병합
    
    # num이 변환할 진수보다 작을 때까지 반복 
    while True:       
        
        # num이 변활할 진수보다 작으면 리스트 마지막에 넣고 반복문 종료
        if num < cmd:
            numList.append(num)
            break
        
        # num을 cmd로 나눈 나머지를 리스트에 넣어주고, 그 몫을 num의 값으로 변경
        else:
            numList.append(num % cmd)
            num = num//cmd
    
    # 리스트를 하나의 문자열로 병합
    for i in numList:
        
            res += insList[i]
    
    # 문자열을 뒤집어서 최종 값 출력
    print(res[::-1] + '\n:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n')
             
    return
       

def main():
    
    print('\n\nThis program will convert a base 10 number into another base\n')
    
    # stop을 입력받을 때까지 반복
    while True:
        num = inputNum() # 정수나 'stop'을 입력받음
        if(num == 'stop'): # stop을 입력받으면 프로그램 종료
            return
        cmd = choice() # 변환할 진수를 입력받음
        calculate(num, cmd) # 진수 변환 계산하고, 결과 값 출력
    
main()