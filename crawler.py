import sys
import requests
import os
from bs4 import BeautifulSoup


r = requests.get('http://www.imdb.com/title/tt0111161/')

b = BeautifulSoup(r.text)
b.find_all(name='span', attrs={'class':'itemprop', 'itemprop':'name'})      #get  name from itemprop all names
x = b.find_all(name='span', attrs={'class':'itemprop', 'itemprop':'name'})
print(x)
print("******************")
b.find(name='span', attrs={'class':'itemprop', 'itemprop':'name'})   #first one
y = b.find(name='span', attrs={'class':'itemprop', 'itemprop':'name'})
print(y.text)
print("**************************************")
az = float(b.find(name='span', attrs={'itemprop':'ratingValue'}).text) # rating values
print(az)
print("*****************")
