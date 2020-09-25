import requests
from bs4 import BeautifulSoup
import smtplib


#URL = 'https://www.aruodas.lt/namai-vilniuje-didziuosiuose-gulbinuose-moletu-pl-3-kambariu-kotedzas-uzmiestyje-uz-studijos-2-1304983/'
URL = 'https://www.aruodas.lt/gyvenamieji-namai/vilniaus-rajone/?FBuildingType=box&FAreaOverAllMin=55&FAreaOverAllMax=150&FPriceMax=100000&FPriceMin=55000'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}


def checkPrice():
	page = requests.get(URL, headers=headers)

	soup = BeautifulSoup(page.content, 'html.parser')

	price = soup.find(class_= "list-item-price").getText()
	price_elements = soup.find_all(class_= "list-item-price")

	for price in price_elements:
		print(price.getText())


"""
def sendEmail(price):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('cantaccessmy@gmail.com', 'zmbhkfepgjwxeltn')

	subject = 'ARUODAS - namas Vilniaus rajone'
	body = f'{price}'

	msg = f"Subject: {subject}\n\n{body}"

	server.sendmail(
		'cantaccessmy@gmail.com',
		'ruta.kalytyte@gmail.com',
		msg
	)

	print("EMAIL HAS BEEN SENT")

	server.quit()
"""


def main():
	checkPrice()


main()