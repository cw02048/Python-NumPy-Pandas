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
    
    return  choice

def displayInventory(theInventory) :
    
    for (author, book) in sorted(theInventory.items()):
        
        print('The author is: ' + author)
        
        for [title, qty, price] in sorted(book):
            
            print('\n       The title is: ' + title + '\n       The qty is: ' + qty + '\n       The price is: ' + price + '\n\n       ----')
          
    return

def displayAuthorsWork(theInventory) :
       
    firstName = input('Enter the author\'s first name: ')
    lastName = input('Enter the author\'s last name: ')
           
    author = lastName.lower() + ', ' + firstName.lower()
     
    if (author.title() in theInventory) == False:
        print('Sorry, but no books by ' + author.title() + ' in the inventory')
    else:
        for [title, qty, price] in sorted(theInventory[author.title()]):
         
            print('       The title is: ' + title + '\n       The qty is: ' + qty + '\n       The price is: ' + price + '\n\n       ----')        
        
        return
          
    return

def addBook(theInventory) :
    
    return

def changePrice(theInventory) :
    
    return

def changeQty(theInventory) :
    
    return

def totalQty(theInventory) :
    
    return

def calculateTotalAmount(theInventory) :
    
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