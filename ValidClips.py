from ClipParser import ClipParser

if __name__ == "__main__":


	inputFilename = "clips.csv"
	parser = ClipParser(inputFilename = inputFilename)

	parser.parse()
