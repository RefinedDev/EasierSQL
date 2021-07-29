# Installation

`pip install EasierSQL`

# EasySQLite code examples -:
Before you proceed, make sure you know Some real SQL, before looking at the code, otherwise you probably won't understand anything.

```py

from EasierSQL import SQLite

database = SQLite.easierSQLite("dataBaseName")

# Creating a table

created_Table = database.create_Table('table_Name','userName TEXT NOT NULL, userID INT PRIMARY KEY')
"""
The second argument is where you write the Column names, their Datatypes and constraints!
Also there is an optional third argument called 'check_if_exists' by default it is True.
"""

print(created_Table) # Returns the result.

# Inserting values into a table.

insert = database.insert_values('table_Name','columns_names','values_here')

print(insert) # Returns the result.

# Getting values from a table

selected_value = database.select_values('table_Name', columnNames='column_Names',limit='1000',clauses='here')
"""
Most of the arguemnts here, have default values for example,
If you leave columnNames blank it will get all the values from the rows by default. 
If you leave limit blank, it will get 100 rows max from the table by default.

In the clauses argument you can add your where clause, cases etc. If left none it won't affect anything.
"""

print(selected_value) # Returns the list of values (or an error).
```

To compensate for no documentation at the moment, here are all the functions.

```py
database.create_Table()
database.select_values()
database.insert_values()
database.delete_table()
database.create_new_column()
database.delete_row()
database.rename_Table()
database.rename_Column()
database.attach_database()
database.detach_database()
database.execute_custom_query() # Returns the database, so you can execute Your own query, if the module doesn't support that type.
```

Example of execute_custom_query()

```py
from EasierSQL import SQLite

database = SQLite.easierSQLite("dataBaseName")

tempDB = database.execute_custom_query()
cursor = tempDB.cursor()

cursor.execute("SQL_QUERY")

# tempDB.commit() COMMIT IF NECESSARY

tempDB.close() # Close database after done with it for good practice.
```