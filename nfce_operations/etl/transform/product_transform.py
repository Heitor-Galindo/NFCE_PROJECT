"""Extract product data from NFCE QRCODE URL"""

import re
from unidecode import unidecode


# def find_children_span(item, index):
#     """Extract item volume, volume type (KG/UN) and unit price"""
#     index = int(index)
#     data = re.sub(
#         r"\s+", "", (item[0].findChildren("span")[index].text).split(":")[1])
#     return data


def product_list(page):
    """Extract product data from NFCE QRCODE URL"""

    product_data = []

    items = page.body.find_all("tr")
    for item in items:
        item = item.findChildren("td")

        item_name = unidecode(
            re.sub(r"\sKg.*$", "", (item[0].span.string))).upper()

        item_volume = float(
            re.sub(",", ".", (item[0].findChildren("span")[2].text).split(":")[1]))
        item_volume_type = (item[0].findChildren("span")[3].text).split(":")[1]
        item_unit_price = float(
            re.sub(",", ".", (item[0].findChildren("span")[4].text).split(":")[1]))

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

        product_data.append(product_row)

    return product_data
