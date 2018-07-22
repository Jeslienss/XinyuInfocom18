from selenium import webdriver
import datetime
import time
from bs4 import BeautifulSoup

counter = 0
endCounter = 1440  # record how many data
interval = 30  # in seconds

# with open('result.csv', 'wb') as f:
while counter < endCounter:
    driver = webdriver.Chrome()
    driver.get('https://ethgasstation.info/')
    pageSource = driver.page_source
    pageSrc = repr(pageSource)
    indexTemp = pageSrc.find('data: [', pageSrc.find('data: [', 0, len(pageSrc)) + 1, len(pageSrc))
    indexStart = pageSrc.find('[', indexTemp, len(pageSrc))
    indexEnd = pageSrc.find(']', indexStart, len(pageSrc))

    soup = BeautifulSoup(pageSource, "lxml")
    table = soup.find_all('table')[0]
    tebleLen = (len(table.find_all('tr')))

    tmpGasPrice = []
    for row in table.findAll('tr')[1:tebleLen]:
        col = row.findAll('td')
        tmpGasPrice.append(col[1].getText())
    tmpGasPrice = ','.join(tmpGasPrice)

    now = datetime.datetime.now()
    CurrentTime = str(now.month) + '-' + str(now.day) + ' ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)
    driver.quit()

    counter = counter + 1
    print(CurrentTime + ',' + pageSrc[indexStart + 1:indexEnd] + ',' + tmpGasPrice + ',')
    # f.write(CurrentTime + ',' + pageSrc[indexStart + 1:indexEnd] + ',' + tmpGasPrice + ',')
    time.sleep(interval)
