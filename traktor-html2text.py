#!/usr/bin/python

from bs4 import BeautifulSoup
from optparse import OptionParser
import os

parser = OptionParser(usage='Usage: %prog filename')

(options, args) = parser.parse_args()
if len(args) != 1:
    parser.error("incorrect number of arguments")
html_file = args[0]

soup = BeautifulSoup(open(html_file))
table = soup.find('table')

playlist = []
for row in table.findAll('tr'):
    cells = row.findAll('td')
    if len(cells):
        title = cells[1].get_text()
        artist = cells[2].get_text()
        playlist.append(unicode(title + ' -- ' + artist))
text_out = '\n'.join(playlist)
#print text_out
filename = os.path.splitext(html_file)[0]
text_file = filename + ".txt"
f = open(text_file, 'w')
f.write(text_out.encode('utf8'))
f.close
