#!/usr/bin/python3
'''
The last exercise in this chapter adds a small feature to the other continuous exercise project, the notebook. In this exercise, add a feature which includes the date and time of the written note to the program. The program works as earlier, but saves data in the form "[note]:::[date and time]" meaning that there is a three-colon separator between the note and timestamp. The timestamp can be generated as follows:




	
>>> import time		

>>> time.strftime("%X %x")
'19:01:34 01/03/09'
>>> 

This returns the date and time in a nice, compact string. When working correctly, the program prints the following:




			
>>> 
(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit

Please select one: 2
Write a new note: Call mom.
(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit

Please select one: 1
Call mom.:::11:44:41 04/25/11

(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit

Please select one: 4
Notebook shutting down, thank you.
>>> 


Example output:
(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit

Please select one: 2
Write a new note: Play football
(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit

Please select one: 1
Play football:::21:11:24 11/04/11

(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit

Please select one: 4
Notebook shutting down, thank you.
The verification of program output does not account for whitespace and is not case-sensitive (the least strict comparison level)
'''

import time

def createNotebook(name):
    try:
        readfiles = open(name, 'r')    
        readfiles.close()
        print("Now using file", name)
    except IOError:
        if name == "notebook.txt":
            print("No default notebook was found, created one.")
        else:
             print("No notebook with that name detected, created one.")
        createFile = open(name, "a")
        print("Now using file ", name)
        createFile.close()
    

def readFile(name):
    try:
        readfile = open(name, 'r')
        content = readfile.read()
        readfile.close()
        print(content)
    except IOError:
        return False



def writeFile(name):
    stringuser = input("Write a new note: ")
    notebook = open(name, "a")    
    check = time.strftime("%X %x")
    all =  stringuser + ":::"+  check + "\n"
    notebook.write(all)
    notebook.close()
def emptyFile():
    newFile = open("notebook.txt", "w+")
    newFile.truncate(0)
    newFile.close()
    print("Notes deleted")

name = "notebook.txt"
option = True
while option == True:
    createNotebook(name)
    print("(1) Read the notebook \n(2) Add note \n(3) Empty the notebook\n(4) Change the notebook \n(5) Quit")
    select = int(input("Please select one:"))
    if (select == 1):
        readFile(name)
    elif (select == 2):
        writeFile(name)
    elif (select == 3):
	    emptyFile()
    elif (select == 4):
        name = input("Give the name of the new file:")
    elif (select == 5):
        option = False
        print("Notebook shutting down, thank you.")

    else:
        print("Incorrect Selection.")
