import requests
from pyteaser import SummarizeUrl
url = 'https://elpais.com/politica/2019/10/14/actualidad/1571033446_440448.html'
#url = 'http://www.huffingtonpost.com/2013/11/22/twitter-forward-secrecy_n_4326599.html'
summaries = SummarizeUrl(url)
print(summaries)

