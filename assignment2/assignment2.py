# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 13:57:46 2019

@author: cw020
"""

import os

#프로그램 실행 시 인사 출력 함수
def greeting() :
    
    print('welcome to the bookstore program!')
    
    return

# 입력한 이름의 파일이 경로에 있는지 확인해주고, 파일을 읽어서 딕셔너리에 저장해주는 함수
def readDatabase(theInventory) :
            
    # 올바른 파일명을 입력할 때까지 반복
    while True :
        
        fileName = input('Enter the name of the file: ')
        
        # 경로에 존재하는 파일명을 입력할 때까지 반복 
        if os.path.isfile(fileName) == True :
            break
        
        else :
            print('Error reading database')
        
    # 파일을 읽어서 딕셔너리에 저장
    parsingDatabase(fileName, theInventory)
      
    return
    
# 파일을 읽어서 딕셔너리에 저장하는 함수
def parsingDatabase(fileName, theInventory):
    
    file = open(fileName)
    
    # 파일의 끝까지 한 줄씩 읽어서 저장
    while True:      
        
        line = file.readline() # 한 줄씩 읽고,
        line = line.rstrip('\n') # 줄바꿈 문자 제거
        
        # 파일의 끝이면 파일을 닫고 함수 종료
        if line == '' :
            file.close()                   
            return
        
        else :
            # ,로 구별하여 리스트에 저장
            line = line.split(',')
            
            # 만약 이미 존재하는 저자명이면 리스트에 합쳐줌
            if line[0] + ', ' + line[1] in theInventory :
                theInventory[line[0] + ', ' + line[1]].append([line[2], line[3], line[4]])               
           
            # 만약 새로 들어가는 저자명이면 새로 저장해줌
            else:
                theInventory.update({line[0] + ', ' + line[1]: [[line[2], line[3], line[4]]]})
            
# 사용자 메뉴를 출력해주는 함수, 입력한 choice를 리턴함
def printMenu() :
    
    print('\n---------------------------------')
    print('Enter 1 to display the inventory')
    print('Enter 2 to display the books by one author')
    print('Enter 3 to add a book')
    print('Enter 4 to change the price')
    print('Enter 5 to change the qty on hand')
    print('Enter 6 to view the total number of books in the inventory')
    print('Enter 7 to see the total amount of the entire inventory')
    print('Enter 8 to exit')
    choice = input('Enter your choice: ')
    
    return choice

# 딕셔너리의 전체 정보를 출력해주는 함수
def displayInventory(theInventory) :
    
    # 저자를 이름 순으로 정렬
    for (author, book) in sorted(theInventory.items()):      
        print('The author is: ' + author)
        
        # 책의 제목 순으로 정렬하여 출력
        for [title, qty, price] in sorted(book):           
            print('\n       The title is: ' + title + '\n       The qty is: ' + qty + '\n       The price is: ' + price + '\n\n       ----')
          
    return

# 원하는 저자의 책 정보를 출력해주는 함수
def displayAuthorsWork(theInventory) :
    
    # 이름의 앞글자들만 대문자로 바꿔줌
    firstName = input('Enter the author\'s first name: ').lower().title()
    lastName = input('Enter the author\'s last name: ').lower().title()
    
    # 저자의 입력 형식을 맞춰줌
    author = lastName + ', ' + firstName
     
    # 딕셔너리에 저자가 없을 때
    if (author in theInventory) == False:      
        print('Sorry, but no books by ' + author + ' in the inventory')       
        return
    
    # 딕셔너리에 저자가 있으면 책의 제목 순으로 출력
    else:             
        for [title, qty, price] in sorted(theInventory[author]):       
            print('       The title is: ' + title + '\n       The qty is: ' + qty + '\n       The price is: ' + price + '\n\n       ----')              
        
        return

# 딕셔너리에 책을 추가하는 함수
def addBook(theInventory) :
    
    # 이름의 앞글자들만 대문자로 바꿔줌
    firstName = input('Enter the author\'s first name: ').lower().title()
    lastName = input('Enter the author\'s last name: ').lower().title() 
    title = input('Enter the title: ').lower().title()
    
    # 저자의 입력 형식을 맞춰줌
    author = lastName + ', ' + firstName
    
    # 이미 책이 존재할 때 메세지 출력
    if checkExisting(author, title, theInventory).isdigit():        
        print('This book is already in the Inventory and cannot be added again')
    
    # 저자만 존재할 때는 책 정보를 입력받아서 출력
    elif checkExisting(author, title, theInventory) == 'existing author':   
        qty = inputQty()
        price = inputPrice()
        theInventory[author].append([title, qty, price])
    
    # 저자가 존재하지 않으면 딕셔너리에 새로운 키과 값을 생성
    else:       
        qty = inputQty()
        price = inputPrice()
        theInventory.update({author: [[title, qty, price]]})
               
    return

# 입력받은 저자와 책 제목이 존재하는지 판별하는 함수
def checkExisting(author, title, theInventory):
    
    # 저자가 존재하는지 확인
    if author in theInventory:   
        cnt = 0
        
        # 책이 존재하는지 확인
        for i in theInventory[author]:
            
            # 책이 존재한다면 몇 번째 리스트에 존재하는지 리턴
            if title in i:         
                return str(cnt)
            cnt += 1
        return 'existing author'  # 저자만 존재할 때 출력
    
    # 저자가 존재하지 않을 때
    else:
        return 'no author'

# 올바른 재고 값을 입력받는 함수
def inputQty():
    
    # 올바른 재고 값을 입력할 때까지 반복
    while True:    
        qty = input('Enter the qty: ')
        
        # 숫자인지 확인
        if(qty.isdigit() == True):
            qty = float(qty)
            
            # 양의 정수인지 확인
            if (qty % 1 == 0 and qty > 0):
                return str(int(qty))
        
        # 잘못된 입력일 경우
        print('Invalid input for qty.')

# 올바른 책의 가격을 입력받는 함수
def inputPrice():
    
    # 올바른 가격을 입력할 때까지 반복
    while True:     
        price = input('Enter the price: ')
        
        # 양의 실수만 받음
        if(len(price) == 4 and price[1] == '.' and price.replace('.', '', 1).isdigit() == True):            
            
            if 0.00 < float(price) <= 9.99:          
                return str(price)
            
        # 잘못된 입력일 경우
        print('Invalid input for price.')
        
    return

# 책의 가격을 변경해주는 함수
def changePrice(theInventory) :
    
    # 이름의 앞글자들만 대문자로 바꿔줌
    firstName = input('Enter the author\'s first name: ').lower().title()
    lastName = input('Enter the author\'s last name: ').lower().title() 
     # 저자의 입력 형식을 맞춰줌
    author = lastName + ', ' + firstName
    
    # 만약 저자가 존재하면
    if author in theInventory:
        title = input('Enter the title: ').lower().title()
        
        # 만약 존재하는 책이면
        if checkExisting(author, title, theInventory).isdigit():
            price = inputPrice() # 바꿀 값을 입력
            print('Price will be updated from ' + theInventory[author][int(checkExisting(author, title, theInventory))][2] + ' to ' + price)
            # 입력받은 값으로 변경
            theInventory[author][int(checkExisting(author, title, theInventory))][2] = price 
        
        # 저자는 있고 책이 없을 때
        else:
            print('No book with the title ' + title + ' by ' + author + ' in inventory.')
    # 저자가 없을 때
    else:
        print('No such author in your database.  So you cannot change the price')
                            
    return

# 책의 재고를 변경해주는 함수
def changeQty(theInventory) :
    
    # 이름의 앞글자들만 대문자로 바꿔줌
    firstName = input('Enter the author\'s first name: ').lower().title()
    lastName = input('Enter the author\'s last name: ').lower().title() 
    # 저자의 입력 형식을 맞춰줌
    author = lastName + ', ' + firstName
        
    # 만약 저자가 존재하면
    if author in theInventory:
        title = input('Enter the title: ').lower().title()
        
        # 만약 존재하는 책이면
        if checkExisting(author, title, theInventory).isdigit():
            qty = inputQty() # 바꿀 값을 입력
            print('Qty will be updated from ' + theInventory[author][int(checkExisting(author, title, theInventory))][1] + ' to ' + qty)
             # 입력받은 값으로 변경
            theInventory[author][int(checkExisting(author, title, theInventory))][1] = qty        
         
        # 저자는 있고 책이 없을 때    
        else:
            print('No book with the title ' + title + ' by ' + author + ' in inventory.')
    # 저자가 없을 때
    else:
        print('No such author in your database.  So you cannot change the qty')
                            
    return

# 책의 재고의 총합을 계산해주는 함수
def totalQty(theInventory) :
    
    total = 0 # 재고를 저장할 변수
    
    # 모든 저자들을 반복
    for author in list(theInventory.keys()): 
        
        # 각 책의 재고 값을 꺼내고 부동소수점 때문에 소수 2번째자리까지 반올림해서 더해줌
        for book in theInventory[author]:
            total = round(total + int(book[1]), 2)
    
    # 결과 값 출력
    print('The total number of books is ' + str(total))
    
    return

# 책의 가격의 총합을 계산해주는 함수
def calculateTotalAmount(theInventory) :
    
    total = 0.00 # 가격을 저장할 변수
    
    # 모든 저자들을 반복
    for author in list(theInventory.keys()):
        
        # 각 책의 재고 값과 가격을 곱해서 tatal에 더해줌 (부동소수점 때문에 소수 2번째자리까지 반올림해서 더해줌)
        for book in theInventory[author]:
            total = round(total + int(book[1]) * float(book[2]), 2)
        
    # 결과 값 출력
    print('The total value of the inventory is $' + str(total))
    
    return

# 메인문
def main() :
    
    theInventory = {}
    greeting()
    readDatabase(theInventory)
    
    while True: 
        
        choice = printMenu()
        
        if choice == '1':
            displayInventory(theInventory)
        elif choice == '2':
            displayAuthorsWork(theInventory)
        elif choice == '3':
            addBook(theInventory)
        elif choice == '4':
            changePrice(theInventory)
        elif choice == '5':
            changeQty(theInventory)
        elif choice == '6':
            totalQty(theInventory)
        elif choice == '7':
            calculateTotalAmount(theInventory)
        elif choice == '8':
            print('Thank you for using this program')
            break
        else :
            print('invalid choice')     
    
    return

main()