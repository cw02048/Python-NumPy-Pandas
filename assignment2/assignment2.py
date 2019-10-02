# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 13:57:46 2019

@author: cw020
"""

import os

def greeting() :
    
    print('welcome to the bookstore program!')
    
    return

def readDatabase(theInventory) :
            
    while True :
        
        fileName = input('Enter the name of the file: ')
        
        if os.path.isfile(fileName) == True :
            break
        
        else :
            print('Error reading database')
        
    parsingDatabase(fileName, theInventory)  
      
    return
    
   
def parsingDatabase(fileName, theInventory):
    
    file = open(fileName)
    
    while True:      
        
        line = file.readline()
        line = line.rstrip('\n')
        
        if line == '' :
            file.close()                   
            return
        
        else :
            line = line.split(',')
            
            if line[0] + ', ' + line[1] in theInventory :
                theInventory[line[0] + ', ' + line[1]].append([line[2], line[3], line[4]])               
           
            else:
                theInventory.update({line[0] + ', ' + line[1]: [[line[2], line[3], line[4]]]})
                

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

def displayInventory(theInventory) :
    
    for (author, book) in sorted(theInventory.items()):      
        print('The author is: ' + author)
        
        for [title, qty, price] in sorted(book):           
            print('\n       The title is: ' + title + '\n       The qty is: ' + qty + '\n       The price is: ' + price + '\n\n       ----')
          
    return

def displayAuthorsWork(theInventory) :
       
    firstName = input('Enter the author\'s first name: ').lower().title()
    lastName = input('Enter the author\'s last name: ').lower().title()
           
    author = lastName + ', ' + firstName
     
    if (author in theInventory) == False:      
        print('Sorry, but no books by ' + author + ' in the inventory')       
        return
    
    else:             
        for [title, qty, price] in sorted(theInventory[author]):       
            print('       The title is: ' + title + '\n       The qty is: ' + qty + '\n       The price is: ' + price + '\n\n       ----')              
        
        return
    
def addBook(theInventory) :
    
    firstName = input('Enter the author\'s first name: ').lower().title()
    lastName = input('Enter the author\'s last name: ').lower().title() 
    title = input('Enter the title: ').lower().title()
    
    author = lastName + ', ' + firstName
    
    if checkExisting(author, title, theInventory).isdigit():        
        print('This book is already in the Inventory and cannot be added again')
        
    elif checkExisting(author, title, theInventory) == 'existing author':   
        qty = inputQty()
        price = inputPrice()
        theInventory[author].append([title, qty, price])
        
    else:       
        qty = inputQty()
        price = inputPrice()
        theInventory.update({author: [[title, qty, price]]})
               
    return

def checkExisting(author, title, theInventory):
    
    if author in theInventory:   
        cnt = 0
        
        for i in theInventory[author]:
            
            if title in i:         
                return str(cnt)
            cnt += 1
        return 'existing author'    
                
    else:
        return 'no author'

def inputQty():
    
    while True:    
        qty = input('Enter the qty: ')
        
        if(qty.isdigit() == True):
            qty = float(qty)
            
            if (qty % 1 == 0 and qty > 0):
                return str(int(qty))
            
        print('Invalid input for qty.')

def inputPrice():
    
    while True:
        
        price = input('Enter the price: ')
        
        if(len(price) == 4 and price[1] == '.' and price.replace('.', '', 1).isdigit() == True):            
            price = float(price)
            
            if 0.00 < price <= 9.99:          
                return str(price)
        
        print('Invalid input for price.')
        
    return

def changePrice(theInventory) :
    
    firstName = input('Enter the author\'s first name: ').lower().title()
    lastName = input('Enter the author\'s last name: ').lower().title() 
    author = lastName + ', ' + firstName
    
    if author in theInventory:
        title = input('Enter the title: ').lower().title()
        
        if checkExisting(author, title, theInventory).isdigit():
            price = inputPrice()
            print('Price will be updated from ' + theInventory[author][int(checkExisting(author, title, theInventory))][2] + ' to ' + price)
            theInventory[author][int(checkExisting(author, title, theInventory))][2] = price
            
        else:
            print('No book with the title ' + title + ' by ' + author + ' in inventory.')
    else:
        print('No such author in your database.  So you cannot change the price')
                            
    return

def changeQty(theInventory) :
    
    firstName = input('Enter the author\'s first name: ').lower().title()
    lastName = input('Enter the author\'s last name: ').lower().title() 
    author = lastName + ', ' + firstName
        
    if author in theInventory:
        title = input('Enter the title: ').lower().title()
        
        if checkExisting(author, title, theInventory).isdigit():
            qty = inputQty()
            print('Qty will be updated from ' + theInventory[author][int(checkExisting(author, title, theInventory))][1] + ' to ' + qty)
            theInventory[author][int(checkExisting(author, title, theInventory))][1] = qty        
            
        else:
            print('No book with the title ' + title + ' by ' + author + ' in inventory.')
    else:
        print('No such author in your database.  So you cannot change the qty')
                            
    return
    
    return

def totalQty(theInventory) :
    
    total = 0
    
    for author in list(theInventory.keys()): 
        
        for book in theInventory[author]:
            total = round(total + int(book[1]), 2)
    
    print('The total number of books is ' + str(total))
    
    return

def calculateTotalAmount(theInventory) :
    
    total = 0.00
    
    for author in list(theInventory.keys()):
        
        for book in theInventory[author]:
            total = round(total + int(book[1]) * float(book[2]), 2)
            
    print('The total value of the inventory is $' + str(total))
    
    return

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