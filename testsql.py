
import sqlite3

db = sqlite3.connect('employee.db')
print("Connection to database setup")
cursor = db.cursor()


cursor.execute(
    ''' 
      CREATE TABLE IF NOT EXISTs employee(id INT NOT NULL UNIQUE,
                                          first_name TEXT NOT NULL,
                                          last_name TEXT,
                                          contact TEXT);
    '''
)

db.commit()

print("Table is created")

cursor.execute(
    '''
      INSERT INTO TABLE employee (id, first_name, last_name, contact)
      VALUES (1, 'John', 'Jacob', 1234);
    '''
)

db.commit()

cursor.execute(
    '''
      SELECT * from employee;
    '''
)

for row in cursor:
  print(row)
