import requests
import re
from database_operations.operations import execute_query
from bs4 import BeautifulSoup
import pandas as pd


def nfce_extractor(link):
    def tag_extractor(index):
        index = int(index)
        data = re.sub(
            "\s+", "", (item[0].findChildren("span")[index].text).split(":")[1]
        )
        return data

    def html_parser(url):
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0"
        }
        http_request = requests.get(url, headers=headers)
        page = BeautifulSoup((http_request.text), "html.parser")
        return page

    item_name = []
    item_volume = []
    item_volume_type = []
    item_unit_price = []
    item_total_value = []
    vendor_name = []
    vendor_cnpj = []
    vendor_address = []

    page = html_parser(link[0])

    items = page.body.find_all("tr")
    for item in items:
        item = item.findChildren("td")

        item_name.append((re.sub("\sKg.*$", "", (item[0].span.string))).upper())
        item_volume.append(float(re.sub(",", ".", (tag_extractor(2)))))
        item_volume_type.append(tag_extractor(3))
        item_unit_price.append(float(re.sub(",", ".", (tag_extractor(4)))))
        item_total_value.append(
            float(re.sub(",", ".", (item[1].findChildren("span")[0].text)))
        )

        vendor_name.append((page.find(class_="txtTopo").text).upper())
        vendor_cnpj.append(
            re.sub("\s+", "", (page.find_all(class_="text")[0].string).split(":")[1])
        )
        vendor_address.append(
            (re.sub("\t+|\n+", "", (page.find_all(class_="text")[1].string))).upper()
        )

    table = pd.DataFrame(
        {
            "PRODUCT": item_name,
            "VOLUME": item_volume,
            "TYPE": item_volume_type,
            "PRICE": item_unit_price,
            "TOTAL": item_total_value,
            "VENDOR": vendor_name,
            "CNPJ": vendor_cnpj,
            "ADDRESS": vendor_address,
        }
    )
    return table


query = "SELECT LINK FROM NFCE_SCHEMA.NFCE_LINKS LIMIT 1"

link_list = execute_query(query)

for link in link_list:
    product_table = nfce_extractor(link)
    print(f"{product_table}\n")
