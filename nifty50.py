import requests
from bs4 import BeautifulSoup

page=requests.get('https://www.moneycontrol.com/indian-indices/nifty-50-9.html')
soup = BeautifulSoup(page.content,'html.parser')

value = soup.find(class_="lastprice").get_text()
print('Nifty50: ',float(value)) #last nifty50 value

value1 = soup.find(class_="change").get_text()
print('change value: ',float(value1)) #change value

value2=round(((float(value1))/float(value))*100,2) #change %
print('Change%: ',str(value2)+'%')

#data from moneycontrol.com(NSE India)
