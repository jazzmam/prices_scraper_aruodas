import requests
from bs4 import BeautifulSoup
import smtplib


URL = 'https://www.aruodas.lt/gyvenamieji-namai/vilniaus-rajone/?FBuildingType=box&FAreaOverAllMin=55&FAreaOverAllMax=150&FPriceMax=100000&FPriceMin=55000'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}


def checkPrice():
	page = requests.get(URL, headers=headers)

	soup = BeautifulSoup(page.content, 'html.parser')


	address_and_link_blocks = soup.find_all(class_= "list-adress")
	price_blocks = soup.find_all(class_= "price")
	area_and_state_blocks = soup.find_all(class_= "list-row")


	for list in address_and_link_blocks:
		address = list.find("h3").find("a").getText()
		link = list.find("h3").find("a").get('href')

		print(address)



	for list in price_blocks:
		price = list.find(class_= "list-item-price")
		price_for_sq_meter = list.find(class_= "price-pm")

		#print(price.getText() + " " + price_for_sq_meter.getText())



	for list in area_and_state_blocks:
		building_area = list.find(class_= "list-AreaOverall")
		land_area = list.find(class_= "list-AreaLot")
		building_state = list.find(class_= "list-HouseStates")

		#if building_state: print(building_state.getText())




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