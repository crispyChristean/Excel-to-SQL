#PLEASE READ BEFORE RUNNING#
#Be sure to provide three arguments when calling from the terminal
#This will be the name of the program ("py programName"), the file destination, and the folder/directory to use
#python new_markII.py all_info filesystem/machine1-data/

#Import all neccassary Modules
import pandas as pandas
import sys
import glob 

#Function checks terminal strings, if not correct, the program will not run
def checking_args():

    if len(sys.argv) > 3:
        print("Too Many Arguments! The First is the program name, second the destination file, and third the folder name!")
        sys.exit(1)
    elif len(sys.argv) < 3:
        print("Too few Arguments! The First is the program name, second the destination file, and third the folder name!")
        sys.exit(1)
    else:
        print("Perfect")
#Function extracts the excel files to then insert into a csv file.
def extracting_excel():
    #Create a dataframe that will hold all dataframes extracted in the directory.
    accumulative_frame = pandas.DataFrame()
    #Variable to associate the file path
    dir = sys.argv[2] 
    #Show the files located within the directory. root_dir is where i is iterating through. 
    for i in glob.iglob('**/*.xlsx', root_dir=dir, recursive=True):
        path = dir + i
        print("File:")
        print(path)
    #Enter a loop within the directory selected
    for file in glob.iglob('**/*.xlsx', root_dir=dir, recursive=True):
        path = dir + file
        print("This is a File:")
        print(path)
        #Create a dataframe or a dictionary that contains multiple dataframes
        temp_frame = pandas.read_excel(path, sheet_name=None)
        #Create a boolean to check if temp_frame is a dictionary.
        checking = isinstance(temp_frame, dict)
        #If true then...
        if checking == True:
                print('Is A Dictionary')
                #When iterating through a dictionary, it'll go through the keys
                for key in temp_frame:
                        #Call the key of the dictionary, doing so will give us the dataframe of a single sheet.
                        individual_dataFrame = (temp_frame[key])
                        #Once we get the sheet, combine the datafframe with the accumulative frame.
                        accumulative_frame = pandas.concat([accumulative_frame, individual_dataFrame])
                        #Repeat until we have gone through all keys within the dictionary

                #Once this loop finishes we then we move on to the next file in the loop. 
        else: 
                #If it isn't a dictionary, we already have it as a dataframe so we just combine it.
                print("Is Not a dictionary")
                accumulative_frame = pandas.concat([accumulative_frame, temp_frame])

    #Once we have gone through all XLSX files, Integrate the accumulative frame into the desired CSV file. 
    print('All Sheets have passed the dataframe integration, inserting into csv file...')
    accumulative_frame.to_csv(sys.argv[1])

#   **PROGRAM BEGINS HERE**
#First check the terminal arguments
checking_args()
#If passes, then extract the files from the given path
extracting_excel()
print("All Done! Files have been inserted to the given csv file or file name!")


#__NOTES__

#   When an excel has multiple sheets, the Dataframe ends up becoming a dictionary,
#the keys end up being the names of each sheet within the excel file and the value becomes the dataframe 
#of that sheet.