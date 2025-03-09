#PLEASE READ BEFORE RUNNING#
#Be sure to provide three arguments when calling from the terminal
#This will be the name of the program ("py programName"), the file destination, and the folder/directory to use

import pandas as pandas
import sys
import glob 


accumulative_frame = pandas.DataFrame()

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
    for file in glob.iglob(f'{sys.argv[2]}**/*.xlsx', recursive=True):
        print(file)

    selected_files = glob.iglob(f'{sys.argv[2]}**/*.xlsx', recursive=True)
    
    organize_data(selected_files)


def organize_data(given):
    

    for iteration in given:
        #Create a temporary frame that reads from one xlsx file.
        temp_frame = pandas.read_excel(iteration)
        pandas.concat([temp_frame, accumulative_frame])
        temp_frame = pandas.DataFrame()
        
    for i in accumulative_frame:
        print(i)

checking_args()
extracting_excel()