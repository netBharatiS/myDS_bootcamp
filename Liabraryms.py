
import datetime


inventory = {
  'Book One' : {'copies' : 5, 'current borrowers' : []},
   'Book Two' : {'copies' : 3, 'current borrowers' : []},
   'Book Three' : {'copies' : 8, 'current borrowers' : []}         
}

user_info = {
  'John' : {'borrowed books : [], '},
  'Johnny' : {'borrowed books : [], '}
}

def checkout_book(book_name, user_name):
  if inventory[book_name]['copies'] > 0 and user_info[user_name]['borrowed_books'] < 3:
    