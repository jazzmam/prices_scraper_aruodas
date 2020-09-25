import requests
from bs4 import BeautifulSoup
import smtplib


URL = 'https://www.aruodas.lt/namai-vilniuje-didziuosiuose-gulbinuose-moletu-pl-3-kambariu-kotedzas-uzmiestyje-uz-studijos-2-1304983/'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}


def checkPrice():
	page = requests.get(URL, headers=headers)

	soup = BeautifulSoup(page.content, 'html.parser')



	title = soup.find(class_= "obj-header-text").getText()
	price = soup.find(class_= "price-eur").getText()
	converted_price = price.strip()


	print(title.strip())
	print(price.strip())

	#if(converted_price )
	sendEmail()


def sendEmail():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('cantaccessmy@gmail.com', 'zmbhkfepgjwxeltn')

	subject = 'ARUODAS - namas Vilniaus rajone'
	body = 'ARUODAS - namas Vilniaus rajone https://www.aruodas.lt/namai-vilniuje-didziuosiuose-gulbinuose-moletu-pl-3-kambariu-kotedzas-uzmiestyje-uz-studijos-2-1304983/'

	msg = f"Subject: {subject}\n\n{body}"

	server.sendmail(
		'cantaccessmy@gmail.com',
		'ruta.kalytyte@gmail.com',
		msg
	)

	print("EMAIL HAS BEEN SENTTTfsfsdfsdf")

	server.quit()



checkPrice()