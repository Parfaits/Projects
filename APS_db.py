import sqlite3
import math

class APS_db():
	"""Handle sqlite3 database operations for AmazonPriceStalker"""
	_conn = sqlite3.connect("APS_client.db")
	_cur = _conn.cursor()

	def __init__(self, user, email=None, price=None, date=None):
		self.user = user
		self.email = email
		self.price = price
		self.date = date

	def _stdev(self, avg):
		# Sample standard deviation of the price over time.
		self._cur.execute(f"SELECT {self.price} FROM {self.user};")
		p = self._cur.fetchall()
		priceList = []
		for x in p:
			priceList.append(x[0])
		n = len(priceList)
		var = []
		for i in range(n):
			var.append((priceList[i] - avg)**2)
		var = sum(var)
		sd = math.sqrt(var/(n-1))
		return sd

	def createClient(self):
		self._cur.execute(f"CREATE TABLE IF NOT EXISTS {self.user} (email text, price real, datestamp text);")
		self._conn.commit()

	def insertValue(self):
		self._cur.execute(f"INSERT INTO {self.user} VALUES ('{self.email}', {self.price}, '{self.date}');")
		self._conn.commit()

	def statistics(self):
		self._cur.execute(f"SELECT AVG(price) FROM {self.user};")
		avg = self._cur.fetchone()
		self._cur.execute(f"SELECT MAX(price) FROM {self.user};")
		maxPrice = self._cur.fetchone()
		self._cur.execute(f"SELECT MIN(price) FROM {self.user};")
		minPrice = self._cur.fetchone()
		self._cur.execute(f"SELECT COUNT(*) FROM {self.user};")
		numEntries = self._cur.fetchone()
		return (minPrice[0], maxPrice[0], numEntries[0], round(avg[0], 2), round(self._stdev(avg[0]), 2))

	def fetch(self, option='*', n=0):
		if option == '*':
			self._cur.execute(f"SELECT * FROM {self.user};")
			return self._cur.fetchall()
		elif option == 1:
			self._cur.execute(f"SELECT * FROM {self.user};")
			return self._cur.fetchone()
		elif option == '+' and n > 0:
			self._cur.execute(f"SELECT * FROM {self.user};")
			return self._cur.fetchmany(n)
		elif option == 't':
			self._cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
			return self._cur.fetchall()
		else:
			print("[DB] option unavailable.")

	def update(self, newPrice):
		self._cur.execute(f"UPDATE {self.user} SET price = {newPrice} WHERE datestamp = {self.date};")
		self._conn.commit()

	def removeRow(self, thisDate):
		self._cur.execute(f"DELETE FROM {self.user} WHERE datestamp = {thisDate};")
		self._cur.execute("VACUUM;")
		self._conn.commit()

	def removeClient(self, thisUser):
		self._cur.execute(f"DROP TABLE IF EXISTS {thisUser};")
		self._cur.execute("VACUUM;")
		self._conn.commit()

	def clearTable(self):
		self.removeClient(self.user)
		self.createClient(self.user)

	def closeConnection(self):
		self._conn.close()
