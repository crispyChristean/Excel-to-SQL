import pandas as pandas
import glob
import sys

accumulative_frame = pandas.DataFrame()
dir = sys.argv[2] 
for i in glob.iglob('**/*.xlsx', root_dir=dir, recursive=True):
        path = dir + i
        print("this is i")
        print(path)

        temp_frame = pandas.read_excel(path, sheet_name=None)
        checking = isinstance(temp_frame, dict)
        print(temp_frame)
        if checking == True:
                print('Is A Dictionary')
                for key in temp_frame:
                        individual_dataFrame = (temp_frame[key])
                        accumulative_frame = pandas.concat([accumulative_frame, individual_dataFrame])
        else: 
                print("Is Not a dictionary")
                accumulative_frame = pandas.concat([accumulative_frame, temp_frame])
accumulative_frame.to_csv("all_info")
# for file in glob.iglob(f'{sys.argv[2]}**/*.xlsx', recursive=True):
#         #Create an instance from the ExcelFile class to check for multiple sheets
#         temp_frame = pandas.read_excel(file, sheet_name=None)
#         print(file)
#         checking = isinstance(temp_frame, dict)
#         print(checking)

#         for i in temp_frame:
#                 print(temp_frame)
        #if checking == False:
                
#python playground.py all_info_two filesystem/machine1-data/