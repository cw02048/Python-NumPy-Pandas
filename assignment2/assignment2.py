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
        
        if (line == '') :
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
    
    return

def displayInventory(theInventory) :
    
    return

def displayAuthorsWork(theInventory) :
    
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
    print(theInventory)
             

main()