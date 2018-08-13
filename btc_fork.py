import urllib.request as urllib2
from bs4 import BeautifulSoup


def find_fork(offset):
    res = []
    page_source = urllib2.urlopen("https://www.blockchain.com/btc/orphaned-blocks?offset=" + str(offset)).read()
    soup = BeautifulSoup(page_source, "lxml")
    table = soup.find_all('table', style='width:auto;border-style:none;')
    for i in range(len(table)):
        res.append(len(table[i].find_all('td', style='width: 235px;')))
    print(offset, res)
    #return res


def main():
    # find_fork(275)
    for x in range(0, 38):
        find_fork(x * 25)


if __name__ == "__main__":
    main()

# tebleLen = (len(table.find_all('tr')))
