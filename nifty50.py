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

value3=soup.find(class_="low").get_text()
real=value3.split(',')
value3=''
for i in range(len(real)):
            value3=value3+real[i]
print('Lowest Value: ',float(value3)) #lowest value

value4=soup.find(class_="high").get_text()
real1=value4.split(',')
value4=''
for i in range(len(real1)):
            value4=value4+real[i]
print('Highest Value: ',float(value4)) #highest value
#data from moneycontrol.com(NSE India)
