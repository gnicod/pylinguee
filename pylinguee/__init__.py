import json, sys
from bs4 import BeautifulSoup
from urllib.request import urlopen

class Linguee:

    def __init__(self, src="espagnol", dest="francais"):
        self.src = src
        self.dest = dest

    def translate(self, query, src=None, dest=None):
        if src is not None:
            self.src = src
        if dest is not None:
            self.dest = dest
        languages = [self.dest, self.src]
        url = "https://www.linguee.fr/%s-%s/traduction/%s.html" % (self.src, self.dest, query)
        webpage = urlopen(url).read()
        soup = BeautifulSoup(webpage, 'html.parser')
        table = soup.find("table",{"id": "result_table"})
        rows = table.find_all("tr")
        highlights = []
        for idrow, row in enumerate(rows):
            hl_row = {}
            for idx, col in enumerate(row.find_all('td')):
                hl_text = ''.join([ b.text for b in col.find_all('b') ])
                hl_row[languages[idx]] = hl_text
            highlights.append(hl_row)
        return highlights

