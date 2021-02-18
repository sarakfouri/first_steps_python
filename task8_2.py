
def readFiles(userinput):
	try:
		readfiles = open(userinput, 'r')
		try:
			content = int(readfiles.readline())
			readfiles.close()
			print("The result was ",1000/content)
		except Exception:
			print("The file contents were unsuitable.")
	except IOError:
		print("There seems to be no file with that name.")

		
userinput = input("Give the file name: ")
readFiles(userinput)


