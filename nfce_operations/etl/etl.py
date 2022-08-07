"""Execute ETL flow"""

import re
from bs4 import BeautifulSoup
from nfce_operations.database_operations.execute_query import execute_query
from nfce_operations.etl.extract.extractor import html_parser
from nfce_operations.etl.transform.product_transform import product_list
from nfce_operations.etl.transform.nfce_transform import nfce_data_list
from nfce_operations.etl.load.loader import load_to_db
from nfce_operations.etl.load.queries import (
    INSERT_PRODUCTS_QUERY, INSERT_NFCE_QUERY, SELECT_LINKS_QUERY)


def run_etl():
    """Execute ETL"""

    links_list = execute_query(SELECT_LINKS_QUERY)

    for link in links_list:
        link = link[0]

        pattern = "^http://www.fazenda"
        url_verify = bool(re.search(pattern, link))

        if url_verify is True:
            print(f"\nExtracting data from: \n{link}")
            page = html_parser(link)
            if isinstance(page, BeautifulSoup):
                print("Extraction successful!")
            else:
                print("Extraction failure!")
                break

            print("Processing product data...")
            product_data = product_list(page)
            if isinstance(product_data, list):
                print("Product data successfuly processed.")
            else:
                print("Failure while processing product data.")
                break

            print("Processing NFCE data...")
            nfce_data = nfce_data_list(page)
            if isinstance(nfce_data, list):
                print("NFCE data successfuly processed.")
            else:
                print("Failure while processing NFCE data.")
                break

            print("Inserting product data into database...")
            result = load_to_db(INSERT_PRODUCTS_QUERY, product_data)
            if result is True:
                print("Product data successfuly inserted.")
            else:
                print("Failure while inserting product data.")
                break

            print("Inserting nfce data into database...")
            result = load_to_db(INSERT_NFCE_QUERY, nfce_data)
            if result is True:
                print("NFCE data successfuly inserted.\n")
            else:
                print("Failure while inserting NFCE data.\n")
                break
        else:
            print("This is not a NFCE link.\nSkipping.\n")
