import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url="https://www.hubertiming.com/results/2018MLK"
html=urlopen(url)

#soup=BeautifulSoup(html, "lxml")
soup=BeautifulSoup(html)

title=soup.title
# print(title)
# print(title.text)

#links=soup.find_all('a')
#print(links)

# links=soup.find_all('a', href=True)
# for i in links:
#     print(i['href'])
data=[]
allrows=soup.find_all("tr")
#print(allrows)
#print(allrows[:5])
for rw in allrows:
    row_list=rw.find_all('td')
#print(row_list)
    dataRow=[]
    for cell in row_list:
    # print(cell.text)
       dataRow.append(cell.text)
    data.append(dataRow)
tils=data[:3]
data=data[1:]
#print(data)
# print(tils)
# print(data[-2:])  

df=pd.DataFrame(data)
print(df)
print(df.head())