import sys

def main():
	outfileName = "defaultOutputFile.txt"
	infileName = "defaultInputFile.txt"
	# cmdline parsing override if-block
	if (len(sys.argv) >= 3):
		#print("Provide the following input >> <name of file to sort alphabetically>.<extension> [space] <name of output file>.<extension>")
		print("Number of arguments: ", len(sys.argv), "arguments.")
		print("Input file: ", str(sys.argv[1]), ", output file: ", str(sys.argv[2]), ".")
		outfileName = str(sys.argv[2])
		infileName = str(sys.argv[1])
	outfile = open(outfileName, "w")
	infile = open(infileName, "r")
	listOfNames = infile.readlines()
	# sortedListOfNames = sortAlphabetically(listOfNames)
	sortedListOfNames = sorted(listOfNames)
	makeAFileWith(sortedListOfNames, outfile)
	outfile.close()
	infile.close()
	print("Done.")
def makeAFileWith(listOfNames, outfile): 
	x = 1
	for name in listOfNames:
		stringToAdd = str(x) + ". " + str(name)
		print(stringToAdd)
		outfile.write(stringToAdd)
		x += 1

if __name__ == '__main__':
	main()
