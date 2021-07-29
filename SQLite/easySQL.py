"""
Make SQLite Easier by using this module. No SQL Commands just methods that do the same thing.
I recommend  you to learn SQL before trying this, because you still have to do some Real SQL.
"""

import sqlite3
import errorTypes

class easierSQLite:
    def __init__(self,databaseName : str):
        self.databaseName =  databaseName

    def create_Table(self,tableName : str,columns_constraintsAndDatatype : str, check_if_exists : bool = True):
        """
        Creates a table based on the arguments, the constraints and the datatype string SHOULD be uppercase, example 'first_Name TEXT NOT NULL, last_Name TEXT NOT NULL' 
        """
        try:
            dataBase = sqlite3.connect(f'{self.databaseName}.DB')
            cursor = dataBase.cursor()

            create_table_string = check_if_exists == True and 'CREATE TABLE IF NOT EXISTS' or 'CREATE TABLE'
            
            cursor.execute(create_table_string + f' {tableName} ({columns_constraintsAndDatatype})')
            dataBase.close()
            return 'Table Created!'
        except Exception as error:
            raise errorTypes.createTableError(error)

    def select_values(self,tableName : str, columnNames : str = '*', limit : str = '100',clauses : str = 'Not specified'):
        """
        Get specific values from the specified table. 
        Limit by default is 100. 
        The values to get from the table is * by default meaning it will get all the values from the rows.
        Clause example -: "WHERE first_NAME = 'refined'"
        """
        try:
            dataBase = sqlite3.connect(f'{self.databaseName}.DB')
            cursor = dataBase.cursor()
            
            if clauses == 'Not specified':
                query = 'SELECT ' + columnNames + ' FROM ' + tableName + ' LIMIT ' + limit 
            else:
                query = 'SELECT ' + columnNames + ' FROM ' + tableName + ' ' + clauses + ' LIMIT ' + limit

            cursor.execute(query)
            result = cursor.fetchall()

            dataBase.close()

            return result
        except Exception as error:
           raise  errorTypes.selectingError(error)

    def insert_values(self,tableName : str,columnNames : str, valuesToInsert: str):
        """
        Insert values into a table. All values need to be specified.
        Example -: insert_values('testTable','first_Name, last_Name','Joe, Biden')
        """
        try:
            dataBase = sqlite3.connect(f'{self.databaseName}.DB')
            cursor = dataBase.cursor()

            query = 'INSERT INTO ' + tableName + f'({columnNames}) ' + f'VALUES ({valuesToInsert})'
            cursor.execute(query)

            dataBase.commit()
            dataBase.close()
            return 'Values Inserted!'
        except Exception as error:
            raise errorTypes.insertingError(error)

    def delete_table(self,tableName: str,check_if_exists : bool = True):
        """
        Drops a table from the database, automatically checks whether the table exists or not. The check can be turned off by setting check_if_exists to false.
        """
        try:
            dataBase = sqlite3.connect(f'{self.databaseName}.DB')
            cursor = dataBase.cursor()

            delete_table_string = check_if_exists == True and 'DROP TABLE IF EXISTS' or 'DROP TABLE'
            cursor.execute(delete_table_string + ' ' + tableName)

            dataBase.close()
            return 'Table dropped!'
        except Exception as error:
            raise errorTypes.delete_table_error(error)

    def create_new_column(self,tableName : str, columnName : str,constraintsAndDatatype : str):
        """
        Add a new columns to an existing table.
        """
        try:
            dataBase = sqlite3.connect(f'{self.databaseName}.DB')
            cursor = dataBase.cursor()

            cursor.execute("ALTER TABLE " + tableName + ' ADD ' + columnName + ' ' + constraintsAndDatatype)

            dataBase.commit()
            dataBase.close()
            return 'Created a new column!'
        except Exception as error:
            raise errorTypes.create_column_error(error)

    def delete_row(self,tableName : str, clauses : str =  None):
        """
        Delete a row from a table, the where clause is optional, but if left empty then everything from the table will be deleted.
        """
        try:
            dataBase = sqlite3.connect(f'{self.databaseName}.DB')
            cursor = dataBase.cursor()
            
            if clauses == None:
                query = 'DELETE FROM ' + tableName
            else:
                query = 'DELETE FROM ' + tableName + ' ' + clauses

            cursor.execute(query)
            
            dataBase.commit()
            dataBase.close()
            return 'Row(s) deleted!'
        except Exception as error:
            raise errorTypes.delete_row_error(error)

    def rename_Table(self,existingTablename : str, newTablename: str):
        """
        Rename an existing table.
        """
        try:
            dataBase = sqlite3.connect(f'{self.databaseName}.DB')
            cursor = dataBase.cursor()

            cursor.execute("ALTER TABLE " + existingTablename + ' RENAME TO ' + newTablename)

            dataBase.commit()
            dataBase.close()

            return 'Table Renamed!'
        except Exception as error:
            raise errorTypes.renameError(error)

    def rename_Column(self,tableName : str, currentColumnname: str,newColumnname : str):
        """
        Rename an existing column in a table.
        """
        try:
            dataBase = sqlite3.connect(f'{self.databaseName}.DB')
            cursor = dataBase.cursor()

            cursor.execute("ALTER TABLE " + tableName + ' RENAME COLUMN ' + currentColumnname + ' TO ' + newColumnname)

            dataBase.commit()
            dataBase.close()

            return 'Column Renamed!'
        except Exception as error:
            raise errorTypes.renameError(error)

    def attach_database(self,databaseNameORlocation : str, aliasName : str):
        """
        Attach a database, to your current Database. If your database is in the same directory as your root file then you can just write the .DB file name, otherwise you will have to write the location of it.
        """
        try:
            dataBase = sqlite3.connect(f'{self.databaseName}.DB')
            cursor = dataBase.cursor()

            cursor.execute("ATTACH DATABASE " + databaseNameORlocation + ' AS ' + aliasName)

            dataBase.close()
            return 'Attached!'
        except Exception as error:
            raise errorTypes.database_attach_error(error)

    def detach_database(self,aliasName : str):
        """
        Detach an attached database from your current database, Arguments passed should be the alias name for the database that you used to attach it earlier.
        """
        try:
            dataBase = sqlite3.connect(f'{self.databaseName}.DB')
            cursor = dataBase.cursor()

            cursor.execute("DETACH DATABASE " + aliasName)

            dataBase.close()
            return 'Attached!'
        except Exception as error:
            raise errorTypes.database_detach_error(error)

    def execute_custom_query(self):
        """
        Returns the database, so you can get the cursor, Run a custom query that is not supported in the module and close the dataBase.
        """
        try:
            dataBase = sqlite3.connect(f'{self.databaseName}.DB')

            return dataBase 
        except Exception as error:
            raise errorTypes.custom_query_error(error)