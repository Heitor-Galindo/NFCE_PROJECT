"""Extract product and NFCE data from QRCODE URL"""

import re
import requests
from bs4 import BeautifulSoup
from unidecode import unidecode


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

    product_list = []

    page = html_parser(url[0])
    items = page.body.find_all("tr")
    for item in items:
        item = item.findChildren("td")
        item_name = unidecode(
            re.sub(r"\sKg.*$", "", (item[0].span.string))).upper()
        item_volume = float(re.sub(",", ".", (tag_extractor(item, 2))))
        item_volume_type = tag_extractor(item, 3)
        item_unit_price = float(re.sub(",", ".", (tag_extractor(item, 4))))
        item_total_value = float(
            re.sub(",", ".", (item[1].findChildren("span")[0].text)))
        nfce_key = re.sub(r"\s+", "", (page.find(class_="chave").string))

        product_row = [
            item_name,
            item_volume,
            item_volume_type,
            item_unit_price,
            item_total_value,
            nfce_key,
        ]

        product_list.append(product_row)

    return product_list


def nfce_extractor(url):
    """Extract data about NFCE itself from QRCODE URL"""

    nfce_data_list = []

    page = html_parser(url[0])
    nfce_key = re.sub(r"\s+", "", (page.find(class_="chave").string))
    nfce_total_value = float(
        re.sub(",", ".", (page.find(class_="totalNumb").string)))
    nfce_tax = float(
        re.sub(",", ".", (page.find(class_="totalNumb txtObs").string)))
    payment_method = unidecode(
        re.sub(r"\s+", "_", (page.find(class_="tx").string)))
    emition_date = timestamp_extractor(page, 0)
    emition_time = timestamp_extractor(page, 1)
    vendor_name = unidecode(page.find(class_="txtTopo").text).upper()
    vendor_cnpj = re.sub(
        r"\s+", "", (page.find_all(class_="text")[0].string).split(":")[1])
    vendor_address = re.sub(
        "\t+|\n+", "", (page.find_all(class_="text")[1].string)).upper()

    nfce_data = [
        vendor_name,
        vendor_cnpj,
        vendor_address,
        emition_date,
        emition_time,
        nfce_total_value,
        nfce_tax,
        nfce_key,
        payment_method,
    ]

    nfce_data_list.append(nfce_data)

    return nfce_data_list
