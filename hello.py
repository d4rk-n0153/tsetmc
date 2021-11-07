#extract text from http://tsetmc.com/tsev2/data/search.aspx?skey=%D8%A7%D8%AE%D8%B2%D8%A7
#importing libraries
import requests,json,pandas as pd, pprint
symbols=[]
numbers=[]
url='http://tsetmc.com/tsev2/data/search.aspx?skey=افاد'

response=requests.get(url)
data=(response.text).split(';')
data.pop()


for d in data:
    #split the string
    d=d.split(',')
    #add the symbol to the list
    symbols.append(d[0])
    #add the number to the list
    numbers.append(d[2])
# #print(symbols,numbers)
dic=dict(zip(symbols,numbers))
# pprint.pprint(dic)
#save dic into text file mode without change text encoding
with open('efad.txt','w',encoding='utf-8') as f:
    f.write(str(dic))