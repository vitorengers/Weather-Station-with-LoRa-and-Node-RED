import datetime
from datetime import date
import os

class Database:

	def logToFile(self, message):
		today = date.today()
		d1 = today.strftime("%d-%m-%Y")
		timestamp = datetime.datetime.now()

		fileName = "log" + str(d1) + ".csv"
		fileExists = os.path.isfile(fileName)

		if (fileExists == True):
			file_object = open(fileName, 'a')
			file_object.write(str(timestamp) + "," + str(message) + "\n")
		else:
			file_object = open(fileName, 'w')
			file_object.write("timestamp,temperature,humidity,light\n")
			file_object.write(str(timestamp) + "," + str(message) + "\n")



	