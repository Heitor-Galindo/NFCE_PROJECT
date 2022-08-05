from struct import pack
import requests
import re
from database_operations.operations import execute_query
from bs4 import BeautifulSoup
import pandas as pd
from unidecode import unidecode


def nfce_extractor(link):
    def tag_extractor(index):
        index = int(index)
        data = re.sub(
            "\s+", "", (item[0].findChildren("span")[index].text).split(":")[1]
        )
        return data

    def timestamp_extractor(index):
        index = int(index)
        timestamp = re.sub(
            "\s+",
            "",
            (page.find("li").find_all("strong")[3].next_sibling).split()[index],
        )
        return timestamp

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
    emition_date = []
    emition_time = []
    nfce_total_value = []
    nfce_tax = []
    nfce_key = []
    payment_method = []

    page = html_parser(link[0])

    items = page.body.find_all("tr")
    for item in items:
        item = item.findChildren("td")

        item_name.append(
            (unidecode(re.sub("\sKg.*$", "", (item[0].span.string)))).upper()
        )
        item_volume.append(float(re.sub(",", ".", (tag_extractor(2)))))
        item_volume_type.append(tag_extractor(3))
        item_unit_price.append(float(re.sub(",", ".", (tag_extractor(4)))))
        item_total_value.append(
            float(re.sub(",", ".", (item[1].findChildren("span")[0].text)))
        )
        payment_method.append(
            unidecode(re.sub("\s+", "_", (page.find(class_="tx").string)))
        )

        vendor_name.append((unidecode(page.find(class_="txtTopo").text)).upper())
        vendor_cnpj.append(
            re.sub("\s+", "", (page.find_all(class_="text")[0].string).split(":")[1])
        )
        vendor_address.append(
            (re.sub("\t+|\n+", "", (page.find_all(class_="text")[1].string))).upper()
        )

        emition_date.append(timestamp_extractor(0))
        emition_time.append(timestamp_extractor(1))

        nfce_tax.append(
            float(re.sub(",", ".", (page.find(class_="totalNumb txtObs").string)))
        )
        nfce_total_value.append(
            float(re.sub(",", ".", (page.find(class_="totalNumb").string)))
        )
        nfce_key.append(re.sub("\s+", "", (page.find(class_="chave").string)))

    product_table = pd.DataFrame(
        {
            "ITEM_NAME": item_name,
            "ITEM_VOLUME": item_volume,
            "ITEM_VOLUME_TYPE": item_volume_type,
            "ITEM_UNIT_PRICE": item_unit_price,
            "ITEM_TOTAL_VALUE": item_total_value,
            "NFCE_KEY": nfce_key,
        }
    )

    nfce_table = pd.DataFrame(
        {
            "NFCE_KEY": nfce_key,
            "NFCE_TOTAL_VALUE": nfce_total_value,
            "NFCE_TAX": nfce_tax,
            "PAYMENT_METHOD": payment_method,
            "EMITION_DATE": emition_date,
            "EMITION_TIME": emition_time,
            "VENDOR_NAME": vendor_name,
            "VENDOR_CNPJ": vendor_cnpj,
            "VENDOR_ADDRESS": vendor_address,
        }
    )

    test_table = pd.DataFrame(
        {
            "ITEM_NAME": item_name,
            "ITEM_VOLUME": item_volume,
            "ITEM_VOLUME_TYPE": item_volume_type,
            "ITEM_UNIT_PRICE": item_unit_price,
            "ITEM_TOTAL_VALUE": item_total_value,
            "PAYMENT_METHOD": payment_method,
            "EMITION_DATE": emition_date,
            "EMITION_TIME": emition_time,
            "VENDOR_NAME": None,
            "VENDOR_CNPJ": None,
            "VENDOR_ADDRESS": None,
            "NFCE_KEY": None,
            "NFCE_TOTAL_VALUE": nfce_total_value,
            "NFCE_TAX": nfce_tax,
        }
    )
    return product_table, nfce_table, test_table


query = "SELECT LINK FROM NFCE_SCHEMA.NFCE_LINKS LIMIT 1"

link_list = execute_query(query)

for link in link_list:
    product_table = nfce_extractor(link)
    print(f"{product_table[1]}\n")
