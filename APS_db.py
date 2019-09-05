import sqlite3
import math

class APS_db():
	"""Handle sqlite3 database operations for AmazonPriceStalker"""
	try:
		_conn = sqlite3.connect("APS_client.db")
		print("[DB] Connected to DB.")
	except sqlite3.Error as e:
		print("[DB] Problem connecting to DB.")
	_cur = _conn.cursor()

	def __init__(self, email, price=None, date=None):
		self.email = email
		self.price = price
		self.date = date

	def _stdev(self, avg):
		# Sample standard deviation of the price.
		self._cur.execute(f"SELECT price FROM '{self.email}';")
		p = self._cur.fetchall()
		priceList = []
		for x in p:
			priceList.append(x[0])
			# print(f"[DB] x={x[0]}")
		n = len(priceList)
		var = []
		for i in range(n):
			var.append((priceList[i] - avg)**2)
			# print(f"[DB] var[{i}]={var[i]}, priceList[{i}]={priceList[i]}")
		var = sum(var)
		sd = math.sqrt(var/(n-1))
		return sd

	def createClient(self):
		self._cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{self.email}';")
		exists = self._cur.fetchone()
		if exists:
			print(f"[DB] Client's table exists for {self.email}.")
		else:
			print("[DB] Created client's table.")
		self._cur.execute(f"CREATE TABLE IF NOT EXISTS '{self.email}' (price REAL, datestamp TEXT);")
		self._conn.commit()

	def insertValue(self):
		self._cur.execute(f"INSERT INTO '{self.email}' VALUES ({self.price}, '{self.date}');")
		self._conn.commit()
		print("[DB] Inserted data into client's table.")

	def statistics(self):
		self._cur.execute(f"SELECT COUNT(*) FROM '{self.email}';")
		numEntries = self._cur.fetchone()
		if numEntries[0] <= 1:
			print("[DB] Not enough entries.")
			return None
		self._cur.execute(f"SELECT AVG(price) FROM '{self.email}';")
		avg = self._cur.fetchone()
		self._cur.execute(f"SELECT MAX(price) FROM '{self.email}';")
		maxPrice = self._cur.fetchone()
		self._cur.execute(f"SELECT MIN(price) FROM '{self.email}';")
		minPrice = self._cur.fetchone()
		stats = (numEntries[0], minPrice[0], maxPrice[0], round(avg[0], 2), round(self._stdev(avg[0]), 2))
		print(f"[DB] Statistics for client {self.email}:")
		print("#Entries\tminPrice\tmaxPrice\tAverage\tStdev")
		print(f"{stats[0]}\t\t{stats[1]}\t\t{stats[2]}\t\t{stats[3]}\t{stats[4]}")
		print('\n')
		return stats

	def fetch(self, option='*', n=0):
		if option == '*':
			self._cur.execute(f"SELECT * FROM '{self.email}';")
			return self._cur.fetchall()
		elif option == 1:
			self._cur.execute(f"SELECT * FROM '{self.email}';")
			return self._cur.fetchone()
		elif option == '+' and n > 0:
			self._cur.execute(f"SELECT * FROM '{self.email}';")
			return self._cur.fetchmany(n)
		elif option == 't':
			self._cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
			return self._cur.fetchall()
		else:
			print("[DB] option unavailable.")

	def update(self, newPrice):
		self._cur.execute(f"UPDATE '{self.email}' SET price = {newPrice} WHERE datestamp = {self.date};")
		self._conn.commit()
		print("[DB] Updated client's table.")

	def removeRow(self, thisDate):
		self._cur.execute(f"DELETE FROM '{self.email}' WHERE datestamp = {thisDate};")
		self._cur.execute("VACUUM;")
		self._conn.commit()
		print(f"[DB] Removed client's row at {thisDate}.")

	def removeClient(self, thisEmail):
		self._cur.execute(f"DROP TABLE IF EXISTS '{thisEmail}';")
		self._cur.execute("VACUUM;")
		self._conn.commit()
		print(f"[DB] Removed client {thisEmail} table.")

	def clearTable(self):
		self.removeClient(self.email)
		self.createClient(self.email)
		print("[DB] Cleared client's table.")

	def closeConnection(self):
		self._conn.close()
		print("[DB] Connection to database closed.")
