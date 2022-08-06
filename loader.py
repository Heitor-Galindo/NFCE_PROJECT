"""Load data to product and nfce table"""

from extractor import product_extractor, nfce_extractor
from database_operations.operations import execute_query, execute_insert

QUERY = "SELECT LINK FROM NFCE_SCHEMA.NFCE_LINKS LIMIT 2"

link_list = execute_query(QUERY)

PRODUCTS_QUERY = """
INSERT INTO NFCE_SCHEMA.NFCE_PRODUCTS (
    ITEM_NAME,
    ITEM_VOLUME,
    ITEM_VOLUME_TYPE,
    ITEM_UNIT_PRICE,
    ITEM_TOTAL_VALUE,
    NFCE_KEY
)
VALUES (%s, %s, %s, %s, %s, %s)"""

NFCE_QUERY = """
INSERT INTO NFCE_SCHEMA.NFCE_DATA (
    VENDOR_NAME,
    VENDOR_CNPJ,
    VENDOR_ADDRESS,
    EMITION_DATE,
    EMITION_TIME,
    NFCE_TOTAL_VALUE,
    NFCE_TAX,
    NFCE_KEY,
    PAYMENT_METHOD
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

for link in link_list:
    product_list = product_extractor(link)
    nfce_list = nfce_extractor(link)
    execute_insert(PRODUCTS_QUERY, product_list)
    execute_insert(NFCE_QUERY, nfce_list)
