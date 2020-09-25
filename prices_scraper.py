import requests
from bs4 import BeautifulSoup
import smtplib


URL = 'https://www.aruodas.lt/gyvenamieji-namai/vilniaus-rajone/?FBuildingType=box&FAreaOverAllMin=55&FAreaOverAllMax=150&FPriceMax=100000&FPriceMin=55000'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}


def checkPrice():
	page = requests.get(URL, headers=headers)

	soup = BeautifulSoup(page.content, 'html.parser')


	all_lists = soup.find_all(class_= "list-row")
	price_blocks = soup.find_all(class_= "price")


	for list in all_lists:
		address = list.select('.list-adress h3 a')
		#post_url = address_block.find('a').get('href')

		building_area = list.find(class_= "list-AreaOverall")
		land_area = list.find(class_= "list-AreaLot")
		building_state = list.find(class_= "list-HouseStates")

		print(address)
		print("AAAA")


	for list in price_blocks:
		price = list.find(class_= "list-item-price")
		price_for_sq_meter = list.find(class_= "price-pm")

		#print(price.getText() + " " + price_for_sq_meter.getText())


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