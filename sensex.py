import requests
from bs4 import BeautifulSoup
page=requests.get('https://www.moneycontrol.com/indian-indices/s&p-bse-sensex-4.html')
soup = BeautifulSoup(page.content,'html.parser')

value = soup.find(class_="lastprice").get_text()
print('Sensex Value: ',float(value)) #last sensex value

value1 = soup.find(class_="change").get_text()
print('Change Value: ',float(value1)) #change value

value2 = round(((float(value1))/float(value))*100,2) #change %
print('Change%: ',str(value2)+'%')

#data from moneycontrol.com(NSE India)



