"""Queries"""

SELECT_LINKS_QUERY = """
SELECT LINK FROM NFCE_SCHEMA.NFCE_LINKS LIMIT 2
"""

INSERT_PRODUCTS_QUERY = """
INSERT INTO NFCE_SCHEMA.NFCE_PRODUCTS (
    ITEM_NAME,
    ITEM_VOLUME,
    ITEM_VOLUME_TYPE,
    ITEM_UNIT_PRICE,
    ITEM_TOTAL_VALUE,
    NFCE_KEY
)
VALUES (%s, %s, %s, %s, %s, %s)"""

INSERT_NFCE_QUERY = """
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
