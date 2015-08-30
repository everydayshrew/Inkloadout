class dataValues:
	def __init__(self):
		 self.values = {"Tank Capacity": 0, "Ink Recovery": 0, "Run": 0, "Swim": 0, "Jump": 0, "Respawn": 0,
		 				"Defense": 0, "Attack": 0, "Charge Rate": 0, "Duration": 0, "Loss Rate": 0}
		 self.data = {}
		 self.calcData()

	def setValue(self, valuename, value): self.values[valuename] = value
	def addMajorValue(self, valuename): self.values[valuename] += 1
	def addMinorrValue(self, valuename): self.values[valuename] += 0.1
	def subtractMajorValue(self, valuename): self.values[valuename] -= 1
	def subtractMinorValue(self, valuename): self.values[valuename] -= 0.1
	def returnValue(self, valuenmae): 
		try: return self.data[valuename] 
		except: return -1

	def returnData(self): return self.data

	def calcData(self):
		# Right now until I can decipher values, this will just return dummy data
		# Tank Capacity
		self.data["Tank Capacity"] = "32.19s"
		# Ink Recovery
		self.data["Ink Recovery"] = "8.32s"
		# Run Speed
		self.data["Run"] = "105%"
		# Swim Speed
		self.data["Swim"] = "105%"
		# Jump Speed
		self.data["Jump"] = "5.12s"
		# Respawn Speed
		self.data["Respawn"] = "6.88s"
		# Defense
		self.data["Defense"] = "112%"
		# Attack
		self.data["Attack"] = "87.3"
		# Charge Rate
		self.data["Charge Rate"] = "102p"
		# Special Duration
		self.data["Duration"] = "5.12s"
		# Special Loss
		self.data["Loss Rate"] = "44%"

