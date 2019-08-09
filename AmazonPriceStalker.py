import requests
import smtplib
import time
from bs4 import BeautifulSoup

URL = 'https://www.amazon.ca/Samsung-Internal-MZ-76E1T0B-AM-Version/dp/B078DPCY3T/ref=sr_1_9?crid=2PE679QWSOLWA&keywords=ssd+1tb&qid=1565223304&s=gateway&sprefix=ss%2Caps%2C222&sr=8-9'
emails = ["", ""]
priceThresh = 9000.0

def log(msg):
	timestamp = time.perf_counter()
	serverLog = f"[{timestamp}] {msg}"
	print(serverLog)

def notify(product, unit, value):
	connection = smtplib.SMTP("smtp.gmail.com", 587)
	connection.ehlo()
	connection.starttls()
	connection.login("", "")

	rcpt = ', '.join(emails)
	log(rcpt)
	subject = "Price dropped for an amazon product!"
	body = f"Product: {product}\nNew price: {unit} {value}\n\nLink: {URL}\n"
	msg = f"From: AmazonPriceStalker <me>\nTo: {rcpt}\nSubject: {subject}\n\n{body}"

	# SMTP.sendmail(from_addr, to_addrs, msg, mail_options=(), rcpt_options=())
	connection.sendmail('', emails, msg)
	log("Mail sent, closing connection.")

	connection.quit()

def checkPrice():
	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36", "Cache-Control": "no-cache", "Pragma": "no-cache"}
	try:
		htmlFile = requests.get(URL, headers=headers, timeout=10)
	except Exception as e:
		raise e
	data = BeautifulSoup(htmlFile.content, 'html.parser')
	productTitle = data.find(id="productTitle").get_text().strip()
	price = data.find(id="priceblock_ourprice").get_text()
	priceBuf = price.split()
	unit = priceBuf[0]
	value = float(priceBuf[1].replace(',', ''))
	date = time.ctime()
	if value < priceThresh:
		log(f"At {date}, the price fell below {priceThresh}")
		log(f"Price now is {price}\n")
		log("Notifying users...")
		notify(productTitle, unit, value)

	log(f"Product: {productTitle}\n\n")
	log(f"Price: {price}")
	log(f"As of {date}")

def main():
	log("Running...\n\n")
	checkPrice()

if __name__ == '__main__':
	main()