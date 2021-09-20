

class Diseases:
	def __init__(self, name, tMin, tMax, hMin, hMax, lMin, lMax):
		self.name = name
		self.tMin = tMin
		self.tMax = tMax
		self.hMin = hMin
		self.hMax = hMax
		self.lMin = lMin
		self.lMax = lMax

	def checkIfPossible(self, t, h, l):
		chance = 0
		if (t >= self.tMin and t <= self.tMax):
			chance = chance + 1
		if (h >= self.hMin and h <= self.hMax): 
			chance = chance + 1
		if (l >= self.lMin and l <= self.lMax):
			chance = chance + 1

		return chance

class Diagnose:
	def __init__(self):
		self.healthy = True
		self.diseases = []

	def addDisease(self, name, tMin, tMax, hMin, hMax, lMin, lMax):
		self.diseases.append(Diseases(name, tMin, tMax, hMin, hMax, lMin, lMax))

	def checkHealth(self, t, h, l):
		result = []
		resultStr = ""
		for i in range(len(self.diseases)):
			result.append(self.diseases[i].checkIfPossible(t, h, l))

		for i in range(len(result)):
			resultStr = resultStr + str(result[i]) + ","

		return resultStr[0:len(resultStr) - 1]




