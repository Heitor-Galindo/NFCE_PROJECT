"""Extract data about NFCE itself from QRCODE URL"""

import re
from unidecode import unidecode
from nfce_operations.etl.transform.nfce_timestamp import nfce_timestamp


def nfce_data_list(page):
    """Extract data about NFCE itself from QRCODE URL"""

    nfce_data = []

    nfce_key = re.sub(r"\s+", "", (page.find(class_="chave").string))
    nfce_total_value = float(
        re.sub(",", ".", (page.find(class_="totalNumb").string)))
    nfce_tax = float(
        re.sub(",", ".", (page.find(class_="totalNumb txtObs").string)))
    payment_method = unidecode(
        re.sub(r"\s+", "_", (page.find(class_="tx").string)))
    emition_date = nfce_timestamp(page, 0)
    emition_time = nfce_timestamp(page, 1)
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

    nfce_data.append(nfce_data)

    return nfce_data
