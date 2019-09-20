# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def inputNum():
    
    while True:
        num = input('Enter an unsigned integer: ')
    
        if(num == 'stop'):
            print('\nThank you for using this program')
            return 'stop'
    
        elif(num.isdigit() == True):
            num = float(num)
        
            if (num % 1 == 0 and num > 0):
                return int(num)
            
def choice():
    
    while True:
        choice = input('b or B for binary, o or O for octal, h or H for hexadecimal: ')
    
        if(choice == 'b' or choice == 'B'):
            return 2
        
        elif(choice == 'o' or choice == 'O'):
            return 8
        
        elif(choice == 'h' or choice == 'H'):
            return 16
        
        else:
            print('\nInvalid choice!')
        
def calculate(num, cmd):
    
    tmp = num
    numList = []
    res = ''
    insList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    
    while True:       
        
        if tmp < cmd:
            numList.append(tmp)
            break
        
        numList.append(tmp % cmd)
        tmp = tmp//cmd
    
    for i in numList:
        
            res += insList[i]
    
    print(res[::-1] + '\n:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n')
             
    return
       

def main():
    
    print('\n\nThis program will convert a base 10 number into another base')
    
    while True:
        num = inputNum()
        if(num == 'stop'):
            return
        cmd = choice()
        calculate(num, cmd)
    
main()