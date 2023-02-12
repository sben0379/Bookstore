import sqlite3

db = sqlite3.connect('ebookstore.db')
cursor = db.cursor()

# Define add book function to collect ID, title, author and qty input from user and add to database. 

def add_book(id, title, author, qty):

    cursor.execute("INSERT INTO books (id, title, author, qty) VALUES (?, ?, ?, ?)", (id, title, author, qty))
    db.commit()

# Define update book function to allow user to select a book by its ID from the databse and change any of its attributes

def update_book(book_id):

    while True:
        try:
            user_input = int(input('''What would you like to update?
            1 - Title
            2 - Author 
            3 - Quantity
            '''))

            if user_input == 1:
                t_input = input('Enter a new title: ')
                cursor.execute('UPDATE books SET TITLE=? WHERE id=?', (t_input, book_id))
            elif user_input == 2:
                a_input = input('Enter a new author: ')
                cursor.execute('UPDATE books SET author=? WHERE id=?', (a_input, book_id))
            elif user_input == 3:
                    while True:
                        try:
                            q_input = int(input("Enter a new quantity: "))
                            cursor.execute('UPDATE books SET qty=? WHERE id=?', (q_input, book_id))
                            break
                        except ValueError:
                            print('Error: Quantity must be a positive integer')
            else:
                print('Error: invalid input.')
            break
        except ValueError:
            print('Error: invalid input.')
        finally:
            db.commit()

# # Define delete book function to allow the user to select a book by its ID from the database and remove it

def delete_book(book_id):

    cursor.execute('DELETE FROM books WHERE id=?', (book_id,))
    db.commit()

# # Define search book function to allow the user to pull a book from the database using either its ID, title or author.

def search_book(book_id):
    
    cursor.execute('SELECT * FROM books WHERE id=?', (book_id,))
    book = cursor.fetchone()
    if book is None:
        print("No book found with ID", book_id)
    else:
        print(book)

# Present user with menu which will continuously display until they choose to exit

while True:

    try:
        menu = int(input('''Select an option:
        1 - Enter book
        2 - Update book
        3 - Delete book
        4 - Search book
        0 - Exit
        '''))

# If 1, ask user to input all required attributes and call add book function. 

        if menu == 1:
            while True:
                try:
                    book_id = int(input("Enter book ID: "))
                    break
                except ValueError:
                    print('Error: ID must be positive integer.')
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            while True:
                try:
                    qty = int(input("Enter book quantity: "))
                    break
                except ValueError:
                    print('Error: quantity must be positive integer.')
            add_book(book_id, title, author, qty)

# If 2, ask user to enter book ID and call update book function.

        elif menu == 2:
            book_id = input("Enter book ID: ")
            update_book(book_id)

# If 3, ask user to enter book ID and call delete book function.

        elif menu == 3:
            book_id = input("Enter book ID: ")
            delete_book(book_id)

# If 4, call search book function.

        elif menu == 4:
            book_id = input("Enter book ID: ")
            search_book(book_id)

# If 0, exit programme. If any other input, print error message. 

        elif menu == 0:
            db.close()
            exit()
        else:
            print('Error: invalid input. Please select an option from the menu.')
    except ValueError:
        print('Error: invalid input. Please select an option from the menu.')