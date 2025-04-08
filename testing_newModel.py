#PLEASE READ BEFORE RUNNING#
#Be sure to provide three arguments when calling from the terminal
#This will be the name of the program ("py programName"), the file destination, and the folder/directory to use
#python testing_newModel.py all_info_four filesystem/machine1-data/
import pandas as pandas
import sys
import glob 
#Glob simply means global.


#Function checks for the arguments given in the terminal, first arg. must be the program name,second the destination
#and the third being the directory the program is under. 
def checking_args():

    if len(sys.argv) > 3:
        print("Too Many Arguments! The First is the program name, second the destination file, and third the folder name!")
        sys.exit(1)
    elif len(sys.argv) < 3:
        print("Too few Arguments! The First is the program name, second the destination file, and third the folder name!")
        sys.exit(1)
    else:
        print("Perfect")

#sys.argv[2] is the file path containing the excel file(s)
#This function extracts all the xlsx files from the directory/folder.
def extracting_excel():
    accumulative_frame = pandas.DataFrame()
    #Checks the last argument in the terminal statement, gets the directory name and finds all xlsx files.
    for file in glob.iglob(f'{sys.argv[2]}**/*.xlsx', recursive=True):
        #Create an instance from the ExcelFile class to check for multiple sheets
        excel = pandas.ExcelFile(file)
        #A variable that associates itself with the number of sheets within an excel file.
        sheet_names = excel.sheet_names

        if len(sheet_names) > 1:
            for eachSheet in sheet_names:
                print(eachSheet)
                temp_frame = pandas.read_excel(eachSheet)
                print(temp_frame)
                accumulative_frame = pandas.concat([temp_frame, accumulative_frame])
        else:
            temp_frame = pandas.read_excel(file)
            print(temp_frame)
            print(accumulative_frame)
            accumulative_frame = pandas.concat([temp_frame, accumulative_frame])
            print('Running Through This')
    print('passes this section')
    accumulative_frame.to_csv("all_info_four")
    
checking_args()
extracting_excel()
