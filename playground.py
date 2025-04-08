import pandas as pandas
import glob
import sys

dir = sys.argv[2] 
for i in glob.iglob('**/*.xlsx', root_dir=dir, recursive=True):
        path = dir + i
        print("this is i")
        print(path)

# for file in glob.iglob(f'{sys.argv[2]}**/*.xlsx', recursive=True):
#         #Create an instance from the ExcelFile class to check for multiple sheets
#         temp_frame = pandas.read_excel(file, sheet_name=None)
#         print(file)
#         checking = isinstance(temp_frame, dict)
#         print(checking)

#         for i in temp_frame:
#                 print(temp_frame)
        #if checking == False:
                
#python playground.py all_info_two filesystem/machine1-data/week1