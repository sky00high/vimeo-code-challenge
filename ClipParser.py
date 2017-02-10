import csv

class ClipParser:
	
	def __init__(self, inputFilename, validFilename="valid.csv", invalidFilename="invalid.csv" ):
		self.inputFilename = inputFilename
		self.validFilename = validFilename
		self.invalidFilename = invalidFilename
		self.indexDict = {}
		self.validIDs = []
		self.invalidIDs = []


	def parseTitleRow(self, row):
		for item in row:
			self.indexDict[item] = row.index(item)

	def ifRowValid(self, row):
		result = True
		clipPrivacy = row[self.indexDict['privacy']]
		if clipPrivacy !=  "anybody":
			result = False
		clipLikes = int(row[self.indexDict['total_likes']])
		if clipLikes < 10:
			result = False
		clipPlays = int(row[self.indexDict['total_plays']])
		if clipPlays < 200:
			result = False
		clipTitle = row[self.indexDict['title']]
		if len(clipTitle) > 30:
			result = False
		return result

	def validInputFile(self):
		with open(self.inputFilename, 'r') as inputFile:

			csvReader = csv.reader(inputFile, delimiter=',')
			titleRow = next(csvReader)
			self.parseTitleRow(titleRow)

			for row in csvReader:
				clipid = row[self.indexDict['id']]
				if self.ifRowValid(row):
					self.validIDs.append([clipid])
				else:
					self.invalidIDs.append([clipid])

	def writeOutputFile(self):

		with open(self.validFilename, 'w', newline='') as validIDFile,\
				open(self.invalidFilename, 'w', newline='') as invalidIDFile:
			validFileWriter = csv.writer(validIDFile)
			validFileWriter.writerows(self.validIDs)

			invalidFileWritter = csv.writer(invalidIDFile)
			invalidFileWritter.writerows(self.invalidIDs)

	def parse(self):
		self.validInputFile()
		self.writeOutputFile()

		





