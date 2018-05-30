import requests
import json

res = requests.get('http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=19910101&stockNo=2330')
data = json.loads(res.text)
print(len(data))