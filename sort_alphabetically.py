def main():
	outfile = open("MGH New Volunteers.txt", "w")
	infile = open("vols.txt", "r")
	listOfVolunteers = infile.readlines()
	# sortedListOfNames = sortAlphabetically(listOfVolunteers)
	sortedListOfNames = sorted(listOfVolunteers)
	makeAFileWith(sortedListOfNames, outfile)
	outfile.close()
	infile.close()

def makeAFileWith(listOfNames, outfile): 
	x = 1
	for name in listOfNames:
		stringToAdd = str(x) + ". " + str(name) + '\n'
		print(stringToAdd)
		outfile.write(stringToAdd)
		x += 1

if __name__ == '__main__':
	main()