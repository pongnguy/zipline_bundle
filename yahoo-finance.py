# script to download all EOD prices from yahoo finance

#%%
import requests
import csv
import json
import time

jsonFilePath = 'download/nasdaq_stocks.json'
with open('download/nasdaq_screener_1628375145418.csv', newline='') as csvFile:
    csvReader = csv.DictReader(csvFile)
    data = {}
    for row in csvReader:
        id = row['Symbol']
        data[id] = row

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
        #all_nasdaq = json.dumps(data, indent=4)

    with open(jsonFilePath, 'r', encoding='utf-8') as jsonf:
        all_nasdaq = json.load(jsonf)
#all_nasdaq = {'TSLA', 'MSFT'}

#%%
for ticker in all_nasdaq:
    # we need to get the cookie
    # "CrumbStore":\{"crumb":"(?<crumb>[^"]+)"\}

    url = 'https://finance.yahoo.com/quote/{0}/history'.format(ticker)  # url for a ticker symbol, with a download link
    r = requests.get(url)  # download page
    print(r)

    txt = r.text  # extract html

    cookie = r.cookies['B']  # the cooke we're looking for is named 'B'
    print('Cookie: ', cookie)

    #print(ticker)
    url = "https://query1.finance.yahoo.com/v7/finance/download/{0}?period1=1596841015&period2=1628377015&interval=1d&events=history&includeAdjustedClose=true".format(ticker)
    print(url)
    r = requests.get(url, allow_redirects=True)
    print(r)
    open('/download/ticker.csv', 'wb').write(r.content)
    #print(url)
    time.sleep(10)