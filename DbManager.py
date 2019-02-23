import sqlite3

#connect to database
db = sqlite3.connect('tour_merchandise.db')

#allows you to access columns by column name
db.row_factory = sqlite3.Row

#create cursor object to execute commands
cur = db.cursor()

#create a tables for the databse if they don't exist
cur.execute('create table if not exists venue(Venue text, Date date, Street text, State text, ZipCode text)')
cur.execute('create table if not exists merchandise(ItemName text, Description text, Price float, Quantity integer)')
cur.execute('create table if not exists sales(Venue text, ItemName text, NumItems integer, '
            'FOREIGN KEY(Venue) REFERENCES venue(Venue), FOREIGN KEY(ItemName) REFERENCES merchandise(ItemName))')

#prints menu selections and gets/returns selection
def main_menu_print():
    print('1. Search')
    print('2. Add Record')
    print('3. Update Record')
    print('4. Delete Record')
    print('5. Exit')
    user_input = int(input('Enter the number of your selection. '))
    return user_input

#used to give the user a choice on which table to add/make changes
def secondary_menu_print():
    #get required information
    print('1. Venue')
    print('2. Merchandise')
    print('3. Sale')
    choice = input('Enter the number of your choice')
    return choice

#method used to query the database
def search_record():

    return

#method to add records to the database
def add_record(choice):
    if choice == 1:
        #get new venue info
        venue = input('What is the venue name? ')
        concertDate = input('What is the concert date? (yyyy-mm-dd) ')
        street = input('What is the street address? ')
        state = input('What state is the venue in?')
        zipCode = input('Enter the Zip Code')
        #add record to database
        cur.execute('insert into venue values(?, ?, ?, ?, ?)', (venue, concertDate, street, state, zipCode))
        #commit the changes
        db.commit()
    elif choice == 2:
        #get new merchandise info
        itemName = input('What is the item name? ')
        description = input('Enter a description of the item. ')
        price = float(input('Enter a price for the item. '))
        quantity = int(input('How many of these do you have? '))
        #add record to database
        cur.execute('insert into merchandise values(?, ?, ?, ?)', (itemName, description, price, quantity))
        #commit the changes
        db.commit()
    elif choice == 3:
        #get sale information
        venue = input('At what venue was this sale completed? ')
        itemName = input('What is the item name? ')
        numItems = input('How many were sold? ')
        #add record to database
        cur.execute('insert into sales values(?, ?, ?)', (venue, itemName, numItems))
        #commit changes
        db.commit()

#method used to update records. Allows you to build an sql string.
def update_record(choice):
    #determine which table to update
    tableName = ''
    if choice == 1:
        tableName = 'venue'
    elif choice == 2:
        tableName = 'merchandise'
    elif choice == 3:
        tableName = 'sales'
    #get update information
    update = input('What field would you like to update? ')
    newValue = input('Enter a new value for this field. ')
    crit = input('Is there any criteria for this update? (y/n)')
    if crit.upper() == 'N':
        #update information
        cur.execute('update ? set ? = ?', (tableName, update, newValue))
        #commit changes
        db.commit()
    elif crit.upper() == 'Y':
        #get criteria
        print('You must enter criteria in this format: (column1 <,>,=, or <> column2)')
        criteria_1 = input('Enter column1. ')
        operator = input('Enter the operator (<,>,=, or <>)')
        criteria_2 = input('Enter column2. ')
        #update the record
        cur.execute("update ? set ? = ? where ?' '?' '?",(tableName, update, newValue, criteria_1, operator, criteria_2))
        #commit changes
        db.commit()

#method used to delete records. Only allows you to delete with criteria.
def delete_record(choice):
    # determine which table to update
    tableName = ''
    if choice == 1:
        tableName = 'venue'
    elif choice == 2:
        tableName = 'merchandise'
    elif choice == 3:
        tableName = 'sales'
    # get update information
    print('You must enter criteria in this format: (column1 <,>,=, or <> column2)')
    criteria_1 = input('Enter column1. ')
    operator = input('Enter the operator (<,>,=, or <>)')
    criteria_2 = input('Enter column2. ')
    #delete the record
    cur.execute("delete from ? where ?' '?' '?", (tableName, criteria_1, operator, criteria_2))
    #commit changes
    db.commit()

#main method
def main():
    #display menu and get user input
    user_input = main_menu_print()
    #call appropriate method
    while user_input != 5:
        if user_input == 1:
            search_record()
        elif user_input == 2:
            print('What do you want to add a new record to?')
            choice = secondary_menu_print()
            add_record(choice)
        elif user_input == 3:
            print('What do you want to update a record for?')
            choice = secondary_menu_print()
            update_record(choice)
        elif user_input == 4:
            print('Where do you want to delete a record from?')
            choice = secondary_menu_print()
            delete_record(choice)
        #re-display the menu
        user_input = main_menu_print()

    #when 5 is selected, exit the program
    exit()


main()