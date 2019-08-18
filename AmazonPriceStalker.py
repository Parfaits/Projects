import requests
import smtplib
import time
from sys import exit
from bs4 import BeautifulSoup

URL = 'https://www.amazon.ca/AmazonBasics-Microfiber-Cleaning-Cloth-24-Pack/dp/B009FUF6DM/ref=pd_ybh_a_4?_encoding=UTF8&psc=1&refRID=9HG1P3PEV20HZJY5FJ81'
emails = ["", ""]
priceThresh = 9000.0

def log(msg):
	timestamp = time.perf_counter()
	serverLog = f"[{timestamp}] {msg}"
	print(serverLog)

def notify(product, price, ex):
	connection = smtplib.SMTP("smtp.gmail.com", 587)
	connection.ehlo()
	connection.starttls()
	connection.login("", "")

	rcpt = ', '.join(emails)
	log(rcpt)
	subject = "[TEST] Price dropped for an amazon product!"
	body = f"Product: {product}\nSpecified threshold: {priceThresh}\nNew price: {price}\n{ex}\n\nLink: {URL}\n"
	msg = f"From: AmazonPriceStalker <me>\nTo: {rcpt}\nSubject: {subject}\n\n{body}"

	# SMTP.sendmail(from_addr, to_addrs, msg, mail_options=(), rcpt_options=())
	log(f"Draft:\n{msg}")
	connection.sendmail('', emails, msg)
	log("Mail sent, closing connection.")

	connection.quit()

def extraInfo(html):
	info = []
	i = 0
	options = html.findAll(class_="olp-padding-right")
	for x in options:
		info.append(x.get_text())
		i += 1
	info = ', '.join(info)
	info = info.replace(u'\xa0', u' ')

	info += "\nAvailability: "
	availability = html.find(id="availability").get_text().strip()
	info += availability.replace(u'\xa0', u' ')

	log(f"Got extra info:\n{info}")
	return info

def checkPrice():
	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36", "Cache-Control": "no-cache", "Pragma": "no-cache"}
	try:
		htmlFile = requests.get(URL, headers=headers, timeout=10)
	except Exception as e:
		raise e
	data = BeautifulSoup(htmlFile.content, 'html.parser')
	productTitle = data.find(id="productTitle").get_text().strip()
	price = data.find(id="priceblock_ourprice").get_text()
	shippingDetails = data.find(id="price-shipping-message").get_text()
	ex = extraInfo(data)

	priceBuf = price.split()
	unit = priceBuf[0]
	value = float(priceBuf[1].replace(',', ''))
	price = price.replace(u'\xa0', u' ')
	shippingDetails = shippingDetails.replace("Details", '')
	shippingDetails = shippingDetails.replace(u'\xa0', u' ')
	price += f" {shippingDetails}"
	date = time.ctime()

	log(f"Product: {productTitle}\n\n")
	log(f"Price: {price}")
	log(f"Shipping Details: {shippingDetails}")
	log(f"As of {date}")

	if value < priceThresh:
		log(f"At {date}, the price fell below {priceThresh}")
		log(f"Price now is {price}\n")
		log("Notifying users...")
		notify(productTitle, price, ex)
	else:
		log(f"Price did not fall below {priceThresh}.")
	log("Done.")

def main():
	log("Running...\n\n")
	while True:
		try:
			checkPrice()
			time.sleep((60*60*60)*24)
			log("Rechecking...\n\n")
		except KeyboardInterrupt:
			log("Shutdown.")
			exit()

if __name__ == '__main__':
	main()