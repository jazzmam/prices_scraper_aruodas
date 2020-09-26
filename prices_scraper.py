import requests
from bs4 import BeautifulSoup
import smtplib
import csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


URL = 'https://www.aruodas.lt/gyvenamieji-namai/vilniaus-rajone/?FBuildingType=box&FAreaOverAllMin=55&FAreaOverAllMax=150&FPriceMax=100000&FPriceMin=55000'
headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}


def collectData():
	page = requests.get(URL, headers=headers)
	page_content = BeautifulSoup(page.content, 'html.parser')


	list_blocks = page_content.find_all(class_= "list-row")


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



def sendEmail():
	email_user = 'cantaccessmy@gmail.com'
	email_password = 'zmbhkfepgjwxeltn'
	email_send = 'ruta.kalytyte@gmail.com'

	subject = 'ARUODAS - namas Vilniaus rajone'

	msg = MIMEMultipart()
	msg['From'] = email_user
	msg['To'] = email_send
	msg['Subject'] = subject

	body = 'Sarasas namu Vilniaus rajone is aruodas.lt yra prisegtam scv dokumente'
	msg.attach(MIMEText(body,'plain'))

	filename='nuosavi_namai_is_aruodo.csv'
	attachment  =open(filename,'rb')

	part = MIMEBase('application','octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition',"attachment; filename= "+filename)

	msg.attach(part)
	text = msg.as_string()
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.starttls()
	server.login(email_user,email_password)


	server.sendmail(email_user,email_send,text)
	server.quit()



def main():
	collectData()
	sendEmail()


main()