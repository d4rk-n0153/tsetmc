#scraping data with jason and requests  and pandas
#creat list for share holders name and number of shares
shareholdersname = []
numberofshares = []
#importing libraries
import requests, json, pandas as pd, pprint
#import library for today date
from datetime import datetime, timedelta
#request from user to input the symbol of the boundry and we search for the symbol in the site with json and requests
symbol_name=input("Enter the symbol of the boundry: ")
response_symbol = requests.get("https://raw.githubusercontent.com/d4rk-n0153/tsetmc/main/market-watch2.html")
symbol_data=json.loads(response_symbol.text)
symbol_number=symbol_data[0].get(symbol_name)
yesterday = datetime.now() - timedelta(1)
yesterday=datetime.strftime(yesterday, '%Y%m%d')
url_json=f'http://cdn.tsetmc.com/api/Shareholder/{symbol_number}/{yesterday}'
print(url_json)
response=requests.get(url_json)
data=json.loads(response.text)
#extracting shareHoldersname and numberofshares from each element of shareShareholder
for person in data['shareShareholder']:
    shareholdersname.append(person['shareHolderName'])
    numberofshares.append(int(person['numberOfShares']))
dic=dict(zip(shareholdersname,numberofshares))
#ذخیره اطلاعات در فایل متنی
with open(f'{symbol_name}.txt', 'w',encoding="utf-8") as f:
    f.write(str(dic))