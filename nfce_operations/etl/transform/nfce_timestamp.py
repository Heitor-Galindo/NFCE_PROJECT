"""Extract time and date from NFCE"""

import re


def nfce_timestamp(page, index):
    """Extract time and date from NFCE"""
    index = int(index)
    timestamp = re.sub(
        r"\s+", "", (page.find("li").find_all("strong")[3].next_sibling).split()[index])
    return timestamp
