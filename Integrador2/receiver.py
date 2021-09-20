import wiringpi

class Receiver:
	def __init__(self):
		wiringpi.wiringPiSetup()
		self.serial = wiringpi.serialOpen('/dev/ttyACM0', 9600)
		self.message = []
		self.hold = ""

	def getLoRaMessage(self, stopChar) -> str:
		while (self.hold != stopChar):	
			self.hold = (chr(wiringpi.serialGetchar(self.serial))) 
			self.message.append(self.hold)

		strMessage = ""
		for i in range (len(self.message) - 1):
			strMessage = strMessage + self.message[i]

		self.message = []
		self.hold = ""
		return strMessage

	def parseLoRaMessage(self, message):
		temp = 0.0
		umi = 0.0
		luz = 0
		if (len(message) > 33):
			temp = float(message[6:11])
			umi = float(message[17:22])
			luz = float(message[28:len(message)])

		print(temp, umi, luz)
