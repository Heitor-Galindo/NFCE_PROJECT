"""Extract product and NFCE data from QRCODE URL"""

import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
from unidecode import unidecode
from database_operations.operations import execute_query


def tag_extractor(item, index):
    """Extract item volume, volume type (KG/UN) and unit price"""
    index = int(index)
    data = re.sub(
        r"\s+", "", (item[0].findChildren("span")[index].text).split(":")[1])
    return data


def timestamp_extractor(page, index):
    """Extract time and date from NFCE"""
    index = int(index)
    timestamp = re.sub(
        r"\s+", "", (page.find("li").find_all("strong")[3].next_sibling).split()[index])
    return timestamp


def html_parser(url):
    """Access NFCE QRCODE URL and return html page"""
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0"}
    http_request = requests.get(url, headers=headers)
    page = BeautifulSoup((http_request.text), "html.parser")
    return page


def product_extractor(url):
    """Extract product data from NFCE QRCODE URL"""

    item_name = []
    item_volume = []
    item_volume_type = []
    item_unit_price = []
    item_total_value = []
    nfce_key = []

    page = html_parser(url[0])
    items = page.body.find_all("tr")
    for item in items:
        item = item.findChildren("td")
        item_name.append(
            (unidecode(re.sub(r"\sKg.*$", "", (item[0].span.string)))).upper())
        item_volume.append(float(re.sub(",", ".", (tag_extractor(item, 2)))))
        item_volume_type.append(tag_extractor(item, 3))
        item_unit_price.append(
            float(re.sub(",", ".", (tag_extractor(item, 4)))))
        item_total_value.append(
            float(re.sub(",", ".", (item[1].findChildren("span")[0].text))))
        nfce_key.append(re.sub(r"\s+", "", (page.find(class_="chave").string)))
    product_table = pd.DataFrame({
        "ITEM_NAME": item_name,
        "ITEM_VOLUME": item_volume,
        "ITEM_VOLUME_TYPE": item_volume_type,
        "ITEM_UNIT_PRICE": item_unit_price,
        "ITEM_TOTAL_VALUE": item_total_value,
        "NFCE_KEY": nfce_key,
    })
    return product_table


def nfce_extractor(url):
    """Extract data about NFCE itself from QRCODE URL"""

    vendor_name = []
    vendor_cnpj = []
    vendor_address = []
    emition_date = []
    emition_time = []
    nfce_total_value = []
    nfce_tax = []
    nfce_key = []
    payment_method = []

    page = html_parser(url[0])
    nfce_key.append(re.sub(r"\s+", "", (page.find(class_="chave").string)))
    nfce_total_value.append(
        float(re.sub(",", ".", (page.find(class_="totalNumb").string))))
    nfce_tax.append(
        float(re.sub(",", ".", (page.find(class_="totalNumb txtObs").string))))
    payment_method.append(
        unidecode(re.sub(r"\s+", "_", (page.find(class_="tx").string))))
    emition_date.append(timestamp_extractor(page, 0))
    emition_time.append(timestamp_extractor(page, 1))
    vendor_name.append(
        (unidecode(page.find(class_="txtTopo").text)).upper())
    vendor_cnpj.append(
        re.sub(r"\s+", "", (page.find_all(class_="text")[0].string).split(":")[1]))
    vendor_address.append(
        (re.sub("\t+|\n+", "", (page.find_all(class_="text")[1].string))).upper())
    nfce_table = pd.DataFrame({
        "NFCE_KEY": nfce_key,
        "NFCE_TOTAL_VALUE": nfce_total_value,
        "NFCE_TAX": nfce_tax,
        "PAYMENT_METHOD": payment_method,
        "EMITION_DATE": emition_date,
        "EMITION_TIME": emition_time,
        "VENDOR_NAME": vendor_name,
        "VENDOR_CNPJ": vendor_cnpj,
        "VENDOR_ADDRESS": vendor_address,
    })
    return nfce_table


QUERY = "SELECT LINK FROM NFCE_SCHEMA.NFCE_LINKS LIMIT 5"

link_list = execute_query(QUERY)
for link in link_list:
    table_product = product_extractor(link)
    table_nfce = nfce_extractor(link)
    print(
        f"---\nPRODUCT_TABLE\n{table_product}\n\nNFCE_TABLE\n{table_nfce}\n---")
