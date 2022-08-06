"""Saves html page for debug"""


def sample_saver(soup):
    """Create a html file for reference"""
    with open("utils/sample.html", "w", encoding="utf8") as file:
        sample = str(soup)
        file.write(sample)
