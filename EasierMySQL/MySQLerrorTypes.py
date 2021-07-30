class createTableError(Exception):
    pass

class selectingError(Exception):
    pass

class insertingError(Exception):
    pass

class delete_table_error(Exception):
    pass

class create_column_error(Exception):
    pass

class delete_row_error(Exception):
    pass

class renameError(Exception):
    pass

class database_attach_error(Exception):
    pass

class database_detach_error(Exception):
    pass

class custom_query_error(Exception):
    pass

class drop_column_error(Exception):
    pass