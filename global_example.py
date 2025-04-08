import pandas as p
import glob
import sys
 
 #Functions HERE
 #Get one row from an already Existing CSV file. 
def checkForIssues(given):
     exit()
     
def fileExample():
 
     temp = ""
     gettingCSV = open("all_info", "r")
     temp = gettingCSV.readline()
     gettingCSV.close()
     #Create an Array that puts the string/line and puts each column name as an element withhin that array.
     save = temp.split(",")
     return save
 
 #Returns a lowercase, no space string.
def cleanString(given):
     #Converts to lowercase
     given = given.casefold()
     #Checks for spaces, removes them if so. 
     for i in given:
         if i.isspace() == True:
             given = given.replace(" ", "")
     #
     if given.isalpha == False:
         print("Sorry, input is invalid, please en-enter")
     else:
         return given
     
 
 
 
 #python testing.py output.csv filesystem/ - use to call the file. 
 
 
 
 
 
 
 
 
 
 #The "Main" function.
def fileSelect():
     
     #Retrieve an example from the recieving file.
     example = fileExample()
     givenFile = input("Please enter the file path: ")
     #Get the CSV file.
     
 
     #possible to integrate a try and except clause later down the line to make a possible path 
     try: 
         #Check if the file extension ends in xlsx
         if (givenFile[-4:]) != "xlsx":
             print("Not an Excel File")
         else: 
             testing = p.read_excel(givenFile) #Place open file in the parathesis 
 
             #Checks if the given xlsx file has the same amount of columns as the csv file it's going to.
             if len(testing.columns)!= (len(example)-1):
                 print("ERROR: The given file has more columns then the recieving file!")
             else:
                 #Using a method to our dataframe, we create a csv file with the values in the dataframe, while specifying 
                 #in the parameter to not include the index. index=False
                 checkForIssues(testing)
                 testing.to_csv("all_info", mode='a', header=False)
 
 #Checks if to repeat
 #Will ask the user if they would like to enter another file. If so, it will call itself to repeat(recursion).
     except FileNotFoundError:
         "The file was not found, please re-enter"
 
 #Retrived all the folders/content in the folder that is WITHIN that folder doesn't also show the content in each folder.
def testingGlob():
     for i in glob.glob("filesystem/**/*.xlsx", recursive=True):
         print(i)
 
 #Gets all the Files within the directory that contains "xlsx"
def stealingExample():  #xlsx is a regular expression, 
     for file in glob.iglob('**/*.xlsx', recursive=True):
         print(file)
 #Basically glob.iglob and glob.glob are methods that search through files recursively.
 
def testing_sys():
     example = fileExample()
     givenFile = input("Please enter the file path: ")
 
     givenFile = sys.argv[1]
 
     print(givenFile)
 
 
 ####PROGRAM BEGINS HERE#######
 #----------------------------#
 
 #testingGlob()
 #fileSelect()
 
 
 
 
 
 
 
 
 #sys.arg is a command line argument is treated like an array and is interacted with similar to an array 
 
 #Using sys.argv[0] shows us the name of the program. It will always be first
 #print(f'Name of the Program: {sys.argv[0]}')
 
 
 #input = sys.argv[1]
 
 #directory_excel = sys.argv[3]