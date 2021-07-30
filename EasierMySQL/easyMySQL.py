from mysql.connector import connect
import MySQLerrorTypes

class easierMySQL():
    def __init__(self,userName : str,passwrd : str,host : str, database : str):
        self.userName = userName
        self.passwrd = passwrd
        self.host = host
        self.database = database

    def create_Table(self,tableName : str,columns_constraintsAndDatatype : str, check_if_exists : bool = True):
        """
        Creates a table based on the arguments, the constraints and the datatype string SHOULD be uppercase, example 'first_Name VARCHAR(35) NOT NULL, last_Name VARCHAR(35) NOT NULL' 
        """
        try:
            dataBase = connect(
                host = self.host,
                user = self.userName,
                passwd = self.passwrd,
                database = self.database
            )

            cursor = dataBase.cursor()

            create_table_string = check_if_exists == True and 'CREATE TABLE IF NOT EXISTS' or 'CREATE TABLE'
            
            cursor.execute(create_table_string + f' {tableName} ({columns_constraintsAndDatatype})')
            dataBase.close()
            return 'Table Created!'
        except Exception as error:
            raise MySQLerrorTypes.createTableError(error)

    def insert_values(self,tableName : str,columnNames : str, valuesToInsert: str):
        """
        Insert values into a table.
        Example -: insert_values('testTable','first_Name, last_Name','Joe, Biden')
        """
        try:
            dataBase = connect(
                host = self.host,
                user = self.userName,
                passwd = self.passwrd,
                database = self.database
            )
            cursor = dataBase.cursor()

            query = 'INSERT INTO ' + tableName + f'({columnNames}) ' + f'VALUES ({valuesToInsert})'
            cursor.execute(query)

            dataBase.commit()
            dataBase.close()
            return 'Values Inserted!'
        except Exception as error:
            raise MySQLerrorTypes.insertingError(error)

    def select_values(self,tableName : str, columnNames : str = '*', limit : str = '100',clauses : str = 'Not specified'):
        """
        Get specific values from the specified table. 
        Limit by default is 100. 
        The values to get from the table is * by default meaning it will get all the values from the rows.
        Clause example -: "WHERE first_NAME = 'refined'"
        """
        try:
            dataBase = connect(
                host = self.host,
                user = self.userName,
                passwd = self.passwrd,
                database = self.database
            )
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
           raise  MySQLerrorTypes.selectingError(error)
    
    def delete_table(self,tableName: str,check_if_exists : bool = True):
        """
        Drops a table from the database, automatically checks whether the table exists or not. The check can be turned off by setting check_if_exists to false.
        """
        try:
            dataBase = connect(
                host = self.host,
                user = self.userName,
                passwd = self.passwrd,
                database = self.database
            )
            cursor = dataBase.cursor()

            delete_table_string = check_if_exists == True and 'DROP TABLE IF EXISTS' or 'DROP TABLE'
            cursor.execute(delete_table_string + ' ' + tableName)

            dataBase.close()
            return 'Table dropped!'
        except Exception as error:
            raise MySQLerrorTypes.delete_table_error(error)

    def create_new_column(self,tableName : str, columnName : str,constraintsAndDatatype : str):
        """
        Add a new columns to an existing table.
        """
        try:
            dataBase = connect(
                host = self.host,
                user = self.userName,
                passwd = self.passwrd,
                database = self.database
            )
            cursor = dataBase.cursor()

            cursor.execute("ALTER TABLE " + tableName + ' ADD ' + columnName + ' ' + constraintsAndDatatype)

            dataBase.commit()
            dataBase.close()
            return 'Created a new column!'
        except Exception as error:
            raise MySQLerrorTypes.create_column_error(error)

    def delete_column(self,tableName : str, columnName : str):
        """
        Delete a column from a table.
        """
        try:
            dataBase = connect(
                host = self.host,
                user = self.userName,
                passwd = self.passwrd,
                database = self.database
            )
            cursor = dataBase.cursor()

            cursor.execute('ALTER TABLE ' + tableName + ' DROP COLUMN ' + columnName)

            dataBase.commit()
            dataBase.close()
            return 'Column dropped!'
        except Exception as error:
            raise MySQLerrorTypes.drop_column_error(error)
    
    def delete_row(self,tableName : str, clauses : str =  None):
        """
        Delete a row from a table, the where clause is optional, but if left empty then everything from the table will be deleted.
        """
        try:
            dataBase = connect(
                host = self.host,
                user = self.userName,
                passwd = self.passwrd,
                database = self.database
            )
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
            raise MySQLerrorTypes.delete_row_error(error)
    
    def rename_Table(self,existingTablename : str, newTablename: str):
        """
        Rename an existing table.
        """
        try:
            dataBase = connect(
                host = self.host,
                user = self.userName,
                passwd = self.passwrd,
                database = self.database
            )
            cursor = dataBase.cursor()

            cursor.execute("ALTER TABLE " + existingTablename + ' RENAME TO ' + newTablename)

            dataBase.commit()
            dataBase.close()

            return 'Table Renamed!'
        except Exception as error:
            raise MySQLerrorTypes.renameError(error)

    def rename_Column(self,tableName : str, currentColumnname: str,newColumnname : str):
        """
        Rename an existing column in a table.
        """
        try:
            dataBase = connect(
                host = self.host,
                user = self.userName,
                passwd = self.passwrd,
                database = self.database
            )
            cursor = dataBase.cursor()

            cursor.execute("ALTER TABLE " + tableName + ' RENAME COLUMN ' + currentColumnname + ' TO ' + newColumnname)

            dataBase.commit()
            dataBase.close()

            return 'Column Renamed!'
        except Exception as error:
            raise MySQLerrorTypes.renameError(error)

    def attach_database(self,databaseNameORlocation : str, aliasName : str):
        """
        Attach a database, to your current Database. If your database is in the same directory as your root file then you can just write the .DB file name, otherwise you will have to write the location of it.
        """
        try:
            dataBase = connect(
                host = self.host,
                user = self.userName,
                passwd = self.passwrd,
                database = self.database
            )
            cursor = dataBase.cursor()

            cursor.execute("ATTACH DATABASE " + databaseNameORlocation + ' AS ' + aliasName)

            dataBase.close()
            return 'Attached!'
        except Exception as error:
            raise MySQLerrorTypes.database_attach_error(error)

    def detach_database(self,aliasName : str):
        """
        Detach an attached database from your current database, Arguments passed should be the alias name for the database that you used to attach it earlier.
        """
        try:
            dataBase = connect(
                host = self.host,
                user = self.userName,
                passwd = self.passwrd,
                database = self.database
            )
            cursor = dataBase.cursor()

            cursor.execute("DETACH DATABASE " + aliasName)

            dataBase.close()
            return 'Detached!'
        except Exception as error:
            raise MySQLerrorTypes.database_detach_error(error)

    def execute_custom_query(self):
        """
        Returns the database, so you can get the cursor, Run a custom query that is not supported in the module and close the dataBase.
        """
        try:
            dataBase = connect(
                host = self.host,
                user = self.userName,
                passwd = self.passwrd,
                database = self.database
            )

            return dataBase 
        except Exception as error:
            raise MySQLerrorTypes.custom_query_error(error)
    
    def show_tables(self):
        """
        Shows all the tables in a database
        """

        dataBase = connect(
            host = self.host,
            user = self.userName,
            passwd = self.passwrd,
            database = self.database
        )

        cursor = dataBase.cursor()
        result = cursor.execute('SHOW TABLES')
        
        dataBase.close()
        return result