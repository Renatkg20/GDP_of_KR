
import requests
import lxml
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
l1 = []
l2 = []
url = 'http://www.stat.kg/ru/opendata/category/2315/xml'

res = requests.get(url)

soup = BeautifulSoup(res.text,'lxml-xml')
titles = soup.find('data').find_all('value')
titles1 = soup.find('data').find_all('key')

for title1 in titles1:
    l1.append(int(title1.get_text()))

for title in titles:
    l2.append(float(title.get_text()))



df = pd.DataFrame({"Year" : l1, 'GDP in USD' : l2})
print(df)
df.plot.hist()


