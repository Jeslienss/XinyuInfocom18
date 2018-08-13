import urllib2
from bs4 import BeautifulSoup

pageSource = urllib2.urlopen("https://www.blockchain.com/btc/orphaned-blocks?offset=25").read()
soup = BeautifulSoup(pageSource, "lxml")
table = soup.find_all('body')[0].find_all('div')[0].find_all('table', recursive=False)


print(len(table[0].find_all('td')))
print(len(table[1].find_all('td')))
print(len(table[2].find_all('td')))
print(len(table[3].find_all('td')))
print(len(table[4].find_all('td')))
print(len(table[5].find_all('td')))
print(len(table[6].find_all('td')))
print(len(table[7].find_all('td')))
print(len(table[8].find_all('td')))
print(len(table[9].find_all('td')))
print(len(table[10].find_all('td')))


# tebleLen = (len(table.find_all('tr')))
