#PLEASE READ BEFORE RUNNING#
#Be sure to provide three arguments when calling from the terminal
#This will be the name of the program ("py programName"), the file destination, and the folder/directory to use
#python new_markII.py all_info_four filesystem/machine1-data/
import pandas as pandas
import sys
import glob 

def checking_args():

    if len(sys.argv) > 3:
        print("Too Many Arguments! The First is the program name, second the destination file, and third the folder name!")
        sys.exit(1)
    elif len(sys.argv) < 3:
        print("Too few Arguments! The First is the program name, second the destination file, and third the folder name!")
        sys.exit(1)
    else:
        print("Perfect")

def extracting_excel():
    accumulative_frame = pandas.DataFrame()
   
    dir = sys.argv[2] 
    for i in glob.iglob('**/*.xlsx', root_dir=dir, recursive=True):
        path = dir + i
        print("this is i")
        print(path)
    
    for i in glob.iglob('**/*.xlsx', root_dir=dir, recursive=True):
        path = dir + i
        excel = pandas.ExcelFile(path)
        sheet_names = excel.sheet_names
        if len(sheet_names) > 1:
            for eachSheet in sheet_names:
                print(eachSheet)
                temp_frame = pandas.read_excel(eachSheet)
                print(temp_frame)
                accumulative_frame = pandas.concat([temp_frame, accumulative_frame])
        else:
            temp_frame = pandas.read_excel(path)
            print(temp_frame)
            print(accumulative_frame)
            accumulative_frame = pandas.concat([temp_frame, accumulative_frame])
            print('Running Through This')

    print('passes this section')
    accumulative_frame.to_csv("all_info_four")
    
checking_args()
extracting_excel()
