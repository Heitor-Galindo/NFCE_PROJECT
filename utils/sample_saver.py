"""Saves html page for debug"""
def sample_saver(soup):
    with open("utils/sample.html", "w") as file:
        sample = str(soup)
        file.write(sample)