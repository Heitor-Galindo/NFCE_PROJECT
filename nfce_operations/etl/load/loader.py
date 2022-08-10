"""Load data to product and nfce table"""

from nfce_operations.database_operations.execute_insert import execute_insert


def load_to_db(query, data_list):
    """Load data to product and nfce table"""
    result = execute_insert(query, data_list)
    if result is True:
        return True
    return False
