import requests
from database_operations.operations import execute_query
from bs4 import BeautifulSoup

query = """
SELECT * FROM NFCE_SCHEMA.NFCE_LINKS LIMIT 1
"""

link = execute_query(query)

for links in link:
    url = links[1]
    print(url)

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0'}
    http_request = requests.get(url, headers=headers)
    page = http_request.text

    soup = BeautifulSoup(page, 'html.parser')
    print(soup.prettify())

