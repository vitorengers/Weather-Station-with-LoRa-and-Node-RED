	
class Parser:

	def parseLoRaMessage(self, message):
		temp = 0.0
		umi = 0.0
		luz = 0
		if (len(message) >= 29):

			temp = (message[message.find("temp") + len("temp: "):message.find("umi") - 1])
			umi = (message[message.find("umi") + len("umi: "):message.find("luz") - 1])
			luz = (message[message.find("luz") + len("luz: "):len(message)])

		return temp, umi, luz   