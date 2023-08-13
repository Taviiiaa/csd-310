#Tavia Payne 
#August 11th 2023
#CYBR 410 Data/database 
#WhatABook Program application 

""" import statements """
import sys
import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

#create methods
def Show_Menu():

    print("\n -- Main Menu --")
    print("\n 1. Display Books\n 2. Display Store Locations\n 3. My Account\n 4. Exit Program\n")

    #user input to navigate the program
    Show_Menu = ["1", "2", "3", "4"]
    choice = input(" PLEASE ENTER THE NUMBER FOR SELECTION! ")
    while choice not in Show_Menu:
        print("\n** INVALID SELECTION: **")
        print("\n 1. Display Books\n 2. Display Store Locations\n 3. My Account\n 4. Exit Program\n")
        choice = input(" PLEASE ENTER THE NUMBER FOR SELECTION! ")
     

    if choice in Show_Menu:
        validChoice = int(choice)
        return validChoice

def Show_Books(cursor):
   # inner join query for book list  

    cursor.execute("SELECT book_id, book_name, author, details FROM book")

     # get the results from the cursor object 
    books = cursor.fetchall()

    print("\n -- BOOK LISTINGS --\n")

    # iterate over the player data set and display the results 
    for B in books:
        print(f" Book Name: {B[1]}\n Book Author: {B[2]}\n Book Details: {B[3]}\n")

def Show_Location(cursor):
    #inner join query for location 

    cursor.execute("SELECT store_id, locale FROM store")

    #get results from cursor object 
    stores = cursor.fetchall()

    print("\n -- CURRENT STORE LOCATIONS -- \n")

     # iterate over the player data set and display the results 
    for i in stores:
        print(f" Location: {i[1]}\n")

def validate_User():
    #Validate the users ID

        print("\n -- ACCOUNT LOGIN --\n")

        validUserIds = ["1", "2", "3"]
        userID = input("PLEASE ENTER YOUR USER ID: ")
        while userID not in validUserIds:
            print("\n** INVALID USER ID. **\n")
            userID = input("PLEASE ENTER YOUR USER ID: ")
            
        if userID in validUserIds:
            validUserIds = int(userID)
            return userID
    
def Show_Account_menu():
    #Display the user account menu
    
    try:
        print("\n-- ACCOUNT MAIN MENU --\n")
        print(" 1. Show Wishlist\n 2. Add A Book To Your Wishlist\n 3. Main Menu\n 4. Exit Program\n")
        
        validAccountOptions = ["1", "2", "3", "4"]
        while True:
            accountOptions = input("\nPLEASE ENTER THE NUMBER FOR SELECTION: ")
            if accountOptions in validAccountOptions:
                validAccountOption = int(accountOptions)
                return validAccountOption
            else:
                print("\n** INVALID SELECTION: **")
    
    except Exception as error:
        print("An error occurred:")

""" DISPLAYING USER WISHLIST METHOD """
def show_wishlist(_cursor, _user_id):
    #Query the database for a list of books
    #two inner joins to combine user and book tables

    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist INNER JOIN user ON wishlist.user_id = user.user_id INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))

    wishlist = _cursor.fetchall()
    
    print("\n -- YOUR WISHLIST BOOKS --\n")
    for i in wishlist:
        print(f" Book Name: {i[4]}\n Author: {i[5]}\n")
    
def show_books_to_add(_cursor, _user_id): 
    #query the database for a list of books not in the wishlist 

    availableBooks = ("SELECT book_id, book_name, author, details FROM book " +
                    "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))     
   
    _cursor.execute(availableBooks)
    booksThatCanBeAdded = _cursor.fetchall()

    print("\n -- BOOKS THAT CAN BE ADDED -- \n")
   
    for i in booksThatCanBeAdded:
        print(f"\n Book ID: {i[0]}\n Book Name: {i[1]}\n")
    
""" ADDING BOOK TO WISHLIST METHOD """
def addBookToWishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, addBookID))






try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config) 
    # connect to the pysports database   

    cursor = db.cursor()

    print("\n WELCOME TO WHATABOOK! ")

    mainMenuSelection = Show_Menu()

    while mainMenuSelection < 4:
        
        if mainMenuSelection == 1:
            Show_Books(cursor) #display books
      

        if mainMenuSelection == 2:
            Show_Location(cursor)  #display location 

        if mainMenuSelection == 3:
            myID = validate_User()
            accountOption = Show_Account_menu() #display account menu
           
            while accountOption != 3:
                
                if accountOption == 1:
                    show_wishlist(cursor, myID) #display wishlist                      
                
                if accountOption == 2:
                    show_books_to_add(cursor, myID)
                    addBookID = input("\nEnter the Book ID you want to add to your wishlist! ")
                    validBookID = ["1", "2", "3", "4", "5", "6", "7", "8", "9"] #add book to wishlist
                   
                    while addBookID not in validBookID:
                        print("\n** invalid Book ID. Please try again! **")
                        addBookID = input("\nEnter the Book ID you want to add to your wishlist! ")
                   
                    if addBookID in validBookID:
                        validBookID = int(addBookID)
                    addBookToWishlist(cursor, myID, validBookID)
                    db.commit()
                    print("\nYour Book was added successfully!")
               
                if accountOption == 4:
                    print("\nProgram Terminated....")
                    sys.exit()
                accountOption = Show_Account_menu() #show account menu
            
        mainMenuSelection = Show_Menu()  #show the main menu
        if mainMenuSelection == 4:
            print("\nProgram Terminated....")
            sys.exit()
      
#handles errors
except mysql.connector.Error as err:
    """ on error code """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """

    db.close()

    #db closed
