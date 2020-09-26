import requests
from bs4 import BeautifulSoup
import smtplib
import csv


URL = 'https://www.aruodas.lt/gyvenamieji-namai/vilniaus-rajone/?FBuildingType=box&FAreaOverAllMin=55&FAreaOverAllMax=150&FPriceMax=100000&FPriceMin=55000'
headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}


def collectData():
	page = requests.get(URL, headers=headers)
	soup = BeautifulSoup(page.content, 'html.parser')


	list_blocks = soup.find_all(class_= "list-row")


	file = open('nuosavi_namai_is_aruodo.csv', 'w')
	writer = csv.writer(file)


	# write header row
	writer.writerow(['Address', 'Price', 'Price for m2', 'Building Area', 'Land Area', 'Building State', 'Link'])


	for elm in list_blocks:
		if not elm.find(class_= "list-adress"): # skip ads
			continue

		address = elm.find("h3").find("a").getText()
		price = elm.find(class_= "price").find(class_= "list-item-price").getText()
		price_for_sq_meter = elm.find(class_= "price").find(class_= "price-pm").getText().strip().replace(' ','')
		link = elm.find("h3").find("a").get('href')
		building_area = elm.find(class_= "list-AreaOverall").getText().strip()
		land_area = elm.find(class_= "list-AreaLot").getText().strip()
		building_state = elm.find(class_= "list-HouseStates").getText().strip()


		writer.writerow([address, price, price_for_sq_meter, building_area, land_area, building_state, link])

	
	file.close()


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
	collectData()


main()