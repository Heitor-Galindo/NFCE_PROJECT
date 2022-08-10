"""test only"""

# import requests

# link = "http://www.fazenda.pr.gov.br/nfce/qrcode?p=41220602178214000188650020003698511201959270|2|1|1|"
# headers = {
#         "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0"}

# r = requests.get(link, headers=headers)
# print(r.url)

import re

LINK = "http://www.fazenda.pr.gov.br/nfce/qrcode?p=2|1|1|"

v = bool(re.search("^http://www.fazenda", LINK))
print(v)
