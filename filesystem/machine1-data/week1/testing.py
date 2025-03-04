import pandas as p

#Functions HERE
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

def fileSelect():
    #MAIN PROGRAM STARTS HERE 

    #Get input to the file path.
    givenFile = input("Please enter the file path: ")

    #possible to integrate a try and except clause later down the line to make a possible path 
    try: 
        #Check if the file extension ends in xlsx
        if (givenFile[-4:]) != "xlsx":
            print("Not an Excel File")

        else: 

            testing = p.read_excel(givenFile) #Place open file in the parathesis 

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


fileSelect()