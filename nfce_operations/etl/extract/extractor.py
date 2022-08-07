"""Extract product and NFCE data from QRCODE URL"""

import requests
from bs4 import BeautifulSoup


def html_parser(url):
    """Access NFCE QRCODE URL and return html page"""
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0"}
    print()
    http_request = requests.get(url[0][0], headers=headers)
    parsed_hmtl = BeautifulSoup((http_request.text), "html.parser")
    return parsed_hmtl
