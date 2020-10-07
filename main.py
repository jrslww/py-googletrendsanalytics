import pandas as pd
from pytrends.request import TrendReq
import tkinter
top = tkinter.Tk()
#Code for access to Google from China
#from pytrends.request import TrendReq
#pytrends = TrendReq(hl='en-US', tz=360, timeout=(10,25), proxies=['https://34.203.233.13:80',], retries=2, backoff_factor=0.1)

pytrend = TrendReq(hl='en-US', tz=360)
n = int(input('Enter a number of tendencies: '))
keywords = []
print("Enter tendencies: ")
for i in range(0, n):
     tend = input()
     keywords.append(tend)
pytrend.build_payload(
     kw_list=keywords,
     cat=0,
     timeframe='today 3-m',
     geo='PL',
     gprop='')
data = pytrend.interest_over_time()
data.to_csv('Py_VS_R.csv', encoding='utf_8_sig')

data = data.drop(labels=['isPartial'],axis='columns')
data.to_csv('Py_VS_R.csv', encoding='utf_8_sig')

image = data.plot(title = (" vs. ".join(keywords)) + ' in last 3 months on Google Trends')
fig = image.get_figure()
fig.savefig('figure.png')

top.mainloop()