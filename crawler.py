import sys
import requests
import os
from bs4 import BeautifulSoup


r = requests.get('http://www.imdb.com/title/tt0111161/')

b = BeautifulSoup(r.text)
b.find_all(name='span', attrs={'class':'itemprop', 'itemprop':'name'})    # too many results
x = b.find_all(name='span', attrs={'class':'itemprop', 'itemprop':'name'})    # too many results
print(x)
print("******************")
b.find(name='span', attrs={'class':'itemprop', 'itemprop':'name'}) # just get the first)
y = b.find(name='span', attrs={'class':'itemprop', 'itemprop':'name'})# just get the first
print(y.text)
print("**************************************")
az = float(b.find(name='span', attrs={'itemprop':'ratingValue'}).text)
print(az)
print("*****************")
