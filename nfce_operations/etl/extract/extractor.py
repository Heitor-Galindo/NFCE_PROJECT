"""Extract product and NFCE data from QRCODE URL"""

import requests
from requests import RequestException
from bs4 import BeautifulSoup

def html_parser(url):
    """Access NFCE QRCODE URL and return html page"""
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0"}
    try:
        http_request = requests.get(url, headers=headers)
    except RequestException as error:
        print(f"Request Error:\n{error}")

    parsed_hmtl = BeautifulSoup((http_request.text), "html.parser")
    return parsed_hmtl
