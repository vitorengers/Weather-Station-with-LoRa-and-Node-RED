from receiver import Receiver
from parser import Parser
from database import Database
from diagnose import Diagnose

class Gateway:
	def __init__(self):
		self._receiver = Receiver()
		self._parser = Parser()
		self._database = Database()
		self._diagnose = Diagnose()
		self._diagnose.addDisease("Ferrugem Comum", 16, 23, 95, 100, 0, 1023)
		self._diagnose.addDisease("Mancha de Phaeosphaeria", 0, 14, 60, 100, 0, 150)
		self._diagnose.addDisease("Ferrugem Tropical", 22, 34, 95, 100, 0, 1023)
		self._diagnose.addDisease("Podridão de Stenocarpella", 28, 30, 95, 100, 0, 1023)
		
	def run(self):
		while(True):
			message = self._receiver.getLoRaMessage("x")
			# print(message)
			temp, umi, luz = self._parser.parseLoRaMessage(message)
			parsedMessage = str(temp) + "," + str(umi) + "," + str(luz)

			diseasesResults = self._diagnose.checkHealth(float(temp), float(umi), int(luz))
			
			if (temp != 0 and umi != 0 and luz != 0):
				self._database.logToFile(parsedMessage + "," + diseasesResults)
				print(parsedMessage + "," + diseasesResults)

