#PLEASE READ BEFORE RUNNING#
#Be sure to provide three arguments when calling from the terminal
#This will be the name of the program ("py programName"), the file destination, and the folder/directory to use
#python copy_of_final.py all_info_three filesystem
#python copy_of_final.py all_info_three filesystem/machine1-data
# Import all neccassary Modules
import pandas as pandas
import sys
import glob 
import sqlite3

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
    destination = sys.argv[1]
    #Show the files located within the directory. root_dir is where i is iterating through to check xlsx files. 
    for i in glob.iglob('**/*.xlsx', root_dir=dir, recursive=True):
        path = dir + i
        print("File:")
        print(path)
        #(path) itself is the file path given in the system arguments combined with the name of the excel file.
        #Think of it as "file_path/current_xlsx_file"

    #Enter a loop within the directory selected
    print("The above Statements show all Excel Files Detected\n")
    for file in glob.iglob('**/*.xlsx', root_dir=dir, recursive=True):
        path = dir + '/' + file
        print("This is a File:")
        print(path)
        #Create a dataframe or a dictionary that contains multiple dataframes
        temp_frame = pandas.read_excel(path, sheet_name=None)
        #Create a boolean to check if temp_frame is a dictionary.
        #If true then...
        if  isinstance(temp_frame, dict):
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
    #This section of the code will be used to sort the Accumulative data frame after sorting it.
    accumulative_frame = accumulative_frame.sort_values(by=['Date', 'Time'], ascending=True, ignore_index=True)

    #organizing_dataFrame(accumulative_frame)
    #Once we have gone through all XLSX files, Integrate the accumulative frame into the desired CSV file. 
    print('All Sheets have passed the dataframe integration, inserting into csv file...')
    accumulative_frame.to_csv(destination)

    #'Final' part of the class is here
    answer_to_write_to = input("Write to a database? \nEnter Y or N: ")
    if answer_to_write_to.casefold() == 'y':
        #
        enter_name = input("Enter the Name of the Database: ")
        enter_table = input("Enter the table you want to write to: ")
        connection = sqlite3.connect(enter_name)
        #Technically Don't need a cursor since to_sql method would technically be doing that?
        cursor = connection.cursor()
        #the parameters to the to_sql method are: table name, connection object, if it exist
        accumulative_frame.to_sql(enter_table, connection, if_exists='append', index=False)
        connection.close()
    else:
         print("You are all set!")

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