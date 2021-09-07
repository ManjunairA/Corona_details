import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://www.worldometers.info/coronavirus/"
r=requests.get(url)
print(r)


html=r.text
soup=BeautifulSoup(html,'html.parser')
print(soup.title.text)
print()
print()
live_data=soup.find_all('div',id='maincounter-wrap')
print(live_data)

for i in live_data:
    print(i.text)
table_body=soup.find("tbody")
table_rows=table_body.find_all('tr')

countries=[]
totalcases=[]
newcases=[]
totaldeaths=[]
todaydeath=[]                     
totalrecoveries=[]
                     
for tr in table_rows:
    td=tr.find_all('td')
    countries.append(td[0].text)
    totalcases.append(td[1].text)
    newcases.append(td[2].text)
    totaldeaths.append(td[3].text)
    todaydeath.append(td[4].text)
    totalrecoveries.append(td[5].text)
                      
headers=['countries','New Cases','Total Cases','Total Deaths','Todays Deaths','Total recoveries']
df=pd.DataFrame(list(zip(countries,newcases,totalcases,totaldeaths,todaydeath,totalrecoveries)),columns=headers)
print(df)
df.to_csv("C:\\Users\\Administrator\\Desktop\\corona_project\\corona_data.csv")
            
                     
