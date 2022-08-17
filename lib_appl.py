# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 01:11:16 2022

@author: 91798
"""
from sys import exit
class Library:
    def __init__(self,list,naam):
        self.naam=naam
        self.bookslist=list
        self.lenddict={}
        
        
    def display_books(self):
        print(f"Following books are available:{self.naam}")
        for book in self.bookslist:
            print(book)
    
    
    def lend_books(self,user,book):
        if book not in self.lenddict.keys():
            self.lenddict.update({book:user})
            print('library database has been updated. Book is now available')
        else:
            print(f"Book has already been lended by {self.lenddict[book]}")
    
    def add_books(self,book):
        self.bookslist.append(book)
        print('Book has been added to the Library database')
    
    def return_books(self,book):
        self.lenddict.pop(book)     
        
if __name__ == '__main__':
    ap=Library("Gyan ka Bhandar",['Python','Scala','Rust','C++','Java','C#','Train to Pakistan','3 men in a Boat'])
    while True:
        print('Welcome to Gyan Ka Bhandar Library. Enter your choice to Continue')
        
        print('Press 1 for displaying List of books')
        print('Press 2 for lending a book')
        print('Press 3 for adding  books')
        print('Press 4 for returning books')
        
        user_choice=input()
        if user_choice not in['1','2','3','4']:
            print("Please enter a valid option")
            continue
        else:
            user_choice=int(user_choice)
            
            
        if user_choice==1:
            ap.display_books()
        elif user_choice==2:
            book=input('Enter the name of book that u wanna lend')
            user=input('Enter your name')
            ap.lend_books(user,book)
        elif user_choice==3:
            book=input("Enter the name of book that u wan't' add to the existing collection")
            ap.add_books(book)
        elif user_choice==4:
            book=input('Enter the name of book that u wanna return to the library')
            ap.return_books(book)
        else:
            print('Not a Valid Option')
            
            
        print('Enter q to quit or c to continue')
        user_input=""
        while(user_input!='q' and user_input!='c'):
            user_input=input()
            if user_input=='q':
                exit()
            elif user_input=='c':
                continue
