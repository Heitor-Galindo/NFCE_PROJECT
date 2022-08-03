import requests
import re
from database_operations.operations import execute_query
from bs4 import BeautifulSoup
import pandas as pd


def nfce_extractor(link):
    def html_parser(url):
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0"
        }
        http_request = requests.get(url, headers=headers)
        html_page = BeautifulSoup((http_request.text), "html.parser")
        return html_page

    page = html_parser(link[0])

    vendor_name = page.find(class_="txtTopo").text

    vendor_cnpj = re.sub(
        "\s+", "", (page.find_all(class_="text")[0].string).split(":")[1]
    )
    vendor_address = re.sub("\t+|\n+", "", (page.find_all(class_="text")[1].string))

    print(
        f"\n ---- \n \
        name: {vendor_name} \n \
        address: {vendor_address} \n \
        cnpj: {vendor_cnpj} \
        \n"
    )

    # for data in vendor_cnpj:

    #     print(f"{data.string} \n------\n")


query = "SELECT LINK FROM NFCE_SCHEMA.NFCE_LINKS LIMIT 1"

link_list = execute_query(query)

for link in link_list:
    nfce_extractor(link)
