from ClipParser import ClipParser, ClipParserReadError, ClipParserWriteError
import argparse

if __name__ == "__main__":

	argparser = argparse.ArgumentParser(description = "Parse clip csv file and validate each entry")
	argparser.add_argument("inputFilename")
	argparser.add_argument("--validoutputfilename", default="valid.csv", help="destination for valid ids",
							dest="validOutputFilename")
	argparser.add_argument("--invalidoutputfilename", default="invalid.csv", help="destination for invalid ids",
							dest="invalidOutputFilename")


	args = argparser.parse_args()

	try:
		parser = ClipParser(inputFilename = args.inputFilename,
							validFilename= args.validOutputFilename,
							invalidFilename = args.invalidOutputFilename)

		parser.parse()
	except ClipParserReadError:
		print("Read error")
	except ClipParserWriteError:
		print("write error")
