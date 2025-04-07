import pandas as pandas
import glob
import sys

for file in glob.iglob(f'{sys.argv[2]}**/*.xlsx', recursive=True):
        #Create an instance from the ExcelFile class to check for multiple sheets
        temp_frame = pandas.read_excel(file)
        
        checking = isinstance(temp_frame, pandas.DataFrame)
        print(checking)
        #if checking == False:
                
#python playground.py all_info_two filesystem/machine1-data