import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://pubmed.ncbi.nlm.nih.gov/?term=%28ERN+OR+CRN+OR+%CE%94+ERN+OR+delta+ERN+OR+delta-ern+OR+ern-crn+OR+Error-related+negativity+OR+correct-related+negativity+OR+error+related+negativity+OR+correct+related+negativity%29+AND+SOCIAL+ANXIETY%29&filter=simsearch1.fha&format=abstract&size=200'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

outfile = open('testsoup.csv','w', newline='')
f = csv.writer(outfile)
f.writerow(["title","doi","abstract"])

titles = soup.findAll('h1', attrs={"class":"heading-title"})
title_array = []
for y in titles:
    title = ([(y.find('a').text)])
    title_array.append(title[0].strip())
title_array = title_array[1::2]

# authors = soup.findAll('div', attrs={"span":"authors-list-item"})
# authors_array = []
# for z in authors:
#     author = ([(z.find('a').text)])
#     authors_array.append(author[0].strip())

# pubs = soup.findAll('div', attrs={"div":"journal-actions dropdown-block"})
# pub_array = []
# for a in pubs:
#     pub = ([(a.find('button').text)])
#     pub_array.append(pub[0].strip())

dois = soup.findAll('div', attrs={"span":"citation-doi"})
doi_array = []
for z in dois:
    doi_array.append(([(z.text)]).strip())

abstracts = soup.findAll('div', attrs={"class":"abstract-content selected"})
abstract_array = []
for x in abstracts:
    abstract = ([(x.find('p').text)])
    abstract_array.append(abstract[0].replace('\n', ' ').strip())

for j in range(len(title_array)):
    f.writerow([title_array[j], dois, abstract_array[j]])