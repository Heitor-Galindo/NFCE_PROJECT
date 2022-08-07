"""Execute ETL flow"""

from nfce_operations.database_operations.execute_query import execute_query
from nfce_operations.etl.extract.extractor import html_parser
from nfce_operations.etl.transform.product_transform import product_list
from nfce_operations.etl.transform.nfce_transform import nfce_data_list
from nfce_operations.etl.load.loader import load_to_db
from nfce_operations.etl.load.queries import (
    INSERT_PRODUCTS_QUERY, INSERT_NFCE_QUERY, SELECT_LINKS_QUERY)


def run_etl():
    """Execute ETL"""
    links = execute_query(SELECT_LINKS_QUERY)
    page = html_parser(links)

    for link in links:
        product_data = product_list(page)
        nfce_data = nfce_data_list(page)
        print(f"\n\n{product_data}\n\n{nfce_data}\n\n")
        load_to_db(INSERT_PRODUCTS_QUERY, product_data)
        load_to_db(INSERT_NFCE_QUERY, nfce_data)
