import pandas as panda
import glob 
#Functions HERE

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
    
#The "Main" function.
def fileSelect():
    #Get input to the file path.
    givenFile = input("Please enter the file path: ")
    #possible to integrate a try and except clause later down the line to make a possible path 
    try: 
        #Check if the file extension ends in xlsx
        if (givenFile[-4:]) != "xlsx":
            print("Not an Excel File")
        else: 
            testing = panda.read_excel(givenFile) #Place open file in the parathesis 

        #Using a method to our dataframe, we create a csv file with the values in the dataframe, while specifying 
        #in the parameter to not include the index. index=False
            testing.to_csv("all_info")

        #Will ask the user if they would like to enter another file. If so, it will call itself to repeat(recursion).
        while True:
            checking = input("Enter another File into the main CSV file?\nenter 'no' OR 'yes': ")
            if cleanString(checking)== "yes":
                fileSelect()
            else:
                exit()

    except FileNotFoundError:
        "The file was not found, please re-enter"

#PROGRAM STARTS HERE

#GLOBAL VARIABLES





givenFile = input("Please enter the file path: ")
#possible to integrate a try and except clause later down the line to make a possible path 
#Check if the file extension ends in xlsx
if (givenFile[-4:]) != "xlsx":
    print("Not an Excel File")
else: 
    #read_excel is both reading the content and storing it in a dataFrame. 
    testing = panda.read_excel(givenFile) #Place open file in the parathesis 
        #Using a method to our dataframe, we create a csv file with the values in the dataframe, while specifying 
        #in the parameter to not include the index. index=False
    #It seems that through printing the object we end up only getting the first row.
    print(testing)
    for i in testing:
        print(i)

    #Even if we did it this way, it would get use the same result, so no matter if we do the 
    #the read_excel method or dataframe Method, 
            ###print('\n')
            ###testing2 = panda.DataFrame(givenFile)
            ###print(testing2)
            ###for i in testing2:
            ####print(i)

    #Through this method, we end up getting all the names of the columns
    #print('\n')
    #print(testing.columns)

#Dataframes are stored as keys, which is why we can't call values like a list.

    #An array to hold the keys.
    holdingKeys = []
    for i in testing:
        holdingKeys.append(i)
    
    #Print the key, doing so will also give us its values.
    #print(holdingKeys)
    print('\n\n\nChecking to see if I can integrate a way to check and adjust values in a column')
    #We can retrive a column by calling the key itself to recieve the value list. 
    #print(testing["Sensor 1"])

    #INTEGRATE into the 
    testing = (testing.round({"Pressure": 1, "Sensor 1": 1, "Sensor 2": 1, "Flow Rate": 1, "Temperature": 1}))
    print(testing)