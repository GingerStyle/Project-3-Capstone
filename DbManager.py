import sqlite3

#connect to database
db = sqlite3.connect('tour_merchandise.db')

#allows you to access columns by column name
db.row_factory = sqlite3.Row

#create cursor object to execute commands
cur = db.cursor()

#create a tables for the databse if they don't exist
cur.execute('create table if not exists venue(Venue text, Date date, Street text, City text, State text, ZipCode text)')
cur.execute('create table if not exists merchandise(ItemName text, Description text, Price float, Quantity integer)')
cur.execute('create table if not exists sales(Venue text, ItemName text, NumItems integer, '
            'FOREIGN KEY(Venue) REFERENCES venue(Venue), FOREIGN KEY(ItemName) REFERENCES merchandise(ItemName))')

#method used to add venues to the database
def add_venue_to_db(venue, concertDate, street, city, state, zipCode):
    try:
        with db:
            cur.execute('insert into venue values(?, ?, ?, ?, ?, ?)', (venue, concertDate, street, city, state, zipCode))
    except sqlite3.Error as error:
        print('Error adding venue.')
        print(error)

#method used to add new merchandise to database
def add_merch_to_db(itemName, description, price, quantity):
    try:
        with db:
            cur.execute('insert into merchandise values(?, ?, ?, ?)', (itemName, description, price, quantity))
    except sqlite3.Error as error:
        print('Error adding merchandise.')
        print(error)

#method used to add sales information to database
def add_sales_to_db(venue, itemName, numItems):
    try:
        with db:
            cur.execute('insert into sales values(?, ?, ?)', (venue, itemName, numItems))
    except sqlite3.Error as error:
        print('Error adding sale.')
        print(error)

#method to perform searches on the venue table
def search_venue(choice, venue, itemName):
    if choice == '1':
        results = cur.execute('select Max(NumItems) from sales group by venue')
        print(results[0])

#method used to perform searches on the merchandise table
def search_merchandise():
    return

#method used to perform searches on the sales table
def search_sales():
    return

#prints menu selections and gets/returns selection
def main_menu_print():
    print('1. Search')
    print('2. Add Venue')
    print('3. Add Merchandise')
    print('4. Add Sales Information')
    print('5. Exit')
    user_input = int(input('Enter the number of your selection. '))
    return user_input

#used to give the user a choice on which table to add/make changes
def secondary_menu_print():
    #get required information
    print('1. Venue')
    print('2. Merchandise')
    print('3. Sale')
    choice = input('Enter the number of your choice. ')
    return choice

#method used to query the database.
def search_record(choice):
    #determine which table to look in
    tableName = ''
    if choice == '1':
        tableName = 'venue'
        print('What search would you like to perform?')
        print('1. How much merchandise was sold at single venue.')
        print('2. Where was the most merchandise sold.')
        print('3. Where was the least merchandise sold.')
        search = input('Enter the number of your choice. ')
        if search == '1':
            venue = input('Enter the name of the venue. ')
            itemName = input('Enter the name of the item. ')
            search_venue(search, venue, itemName)
        elif search == '2':
            search_venue(2)
    elif choice == '2':
        tableName = 'merchandise'
        print('What search would you like to perform?')
        print('1. ')
        print('2. ')
        search = input('Enter the number of your choice. ')
        if search == '1':
            search_merchandise()
    elif choice == '3':
        tableName = 'sales'
        print('What search would you like to perform?')
        print('1. How much merchandise was sold at single venue.')
        print('2. What is the biggest seller.')
        print('3. What sells the least.')

    #print the results

#method to add records to the database
def add_venue():
    venue = input('What is the venue name? ')
    concertDate = input('What is the concert date? (yyyy-mm-dd) ')
    street = input('What is the street address? ')
    city = input('What city is the venue in? ')
    state = input('What state is the venue in? ')
    zipCode = input('Enter the Zip Code. ')
    #add record to database
    add_venue_to_db(venue, concertDate, street, city, state, zipCode)

def add_merchandise():
    #get new merchandise info
    itemName = input('What is the item name? ')
    description = input('Enter a description of the item. ')
    price = float(input('Enter a price for the item. '))
    quantity = int(input('How many of these do you have? '))
    #add record to database
    add_merch_to_db(itemName, description, price, quantity)

def add_sales():
    #get sale information
    venue = input('At what venue was this sale completed? ')
    itemName = input('What is the item name? ')
    numItems = input('How many were sold? ')
    #add record to database
    add_sales_to_db(venue, itemName, numItems)

#main method
def main():
    #display menu and get user input
    user_input = main_menu_print()
    #call appropriate method
    while user_input != 5:
        if user_input == 1:
            print('Where do you want to search?')
            choice = secondary_menu_print()
            search_record(choice)
        elif user_input == 2:
            add_venue()
        elif user_input == 3:
            add_merchandise()
        elif user_input == 4:
            add_sales()
        #re-display the menu
        user_input = main_menu_print()

    #when 5 is selected, exit the program
    exit()


main()