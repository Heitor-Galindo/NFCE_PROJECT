import requests
import re
from database_operations.operations import execute_query
from bs4 import BeautifulSoup
from unidecode import unidecode

def nfce_extractor(link):
    def html_parser(url):
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0"
        }
        http_request = requests.get(url, headers=headers)
        html_page = BeautifulSoup((http_request.text), "html.parser")
        return html_page

    page = html_parser(link[0])

    value = unidecode(re.sub("\s+", "_", (page.find(class_="tx").string)))


    print(
f"\n \
---- \n \
{value} \n \
---- \n\n"
    )

    # for data in vendor_cnpj:

    #     print(f"{data.string} \n------\n")


query = "SELECT LINK FROM NFCE_SCHEMA.NFCE_LINKS LIMIT 1"

link_list = execute_query(query)

for link in link_list:
    nfce_extractor(link)
