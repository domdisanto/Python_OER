# -*- coding: utf-8 -*-
"""
FAERS Use Case Check Script
Written: 12/23/2020
Updated: 12/23/2020
@author: Dominic DiSanto
"""


# Module Import 
import pandas as pd
#import numpy as np 
import os.path 

print('Solution script executing...')

# Importing solution csv from GitHub 
solution_df = pd.read_csv(r'https://raw.githubusercontent.com/domdisanto/Python_OER_Private/main/Rahim_FAERS/Instructor%20Materials/FAERS_Solution.csv?token=AIJQKGBBHOJHSF6MIPFKLT274UDOC')


# Identifying student submission filepaths

filepath = r'C:\Users\Dominic DiSanto\Documents\Python_OER\Use Cases\FAERS_DataPull\\'
#python_sub = r'C:\Users\Dominic DiSanto\Documents\Python_OER\Use Cases\FAERS_DataPull\FY2019_PhenytoinAERS_Python.csv'
#R_sub = r'C:\Users\Dominic DiSanto\Documents\Python_OER\Use Cases\FAERS_DataPull\FY2019_PhenytoinAERS_R.csv'
#general_sub = r'C:\Users\Dominic DiSanto\Documents\Python_OER\Use Cases\FAERS_DataPull\FY2019_PhenytoinAERS.csv'

python_sub_fp = r'FY2019_PhenytoinAERS_Python.xlsx'
R_sub_fp = r'FY2019_PhenytoinAERS_R.xlsx'
general_sub_fp = r'FY2019_PhenytoinAERS.xlsx'

data = filepath + python_sub_fp


# Creating a function to chek student submissions across solution data frame
def solution_check(data):
    # Importing python file
    student_sub = pd.read_excel(data)
    
    # Checking if index is present and deleting if so:
    if 'Unnamed: 0' in student_sub .columns:
        index_bool = True
        del student_sub ['Unnamed: 0']
    else:
        index_bool = False
        
    if set(student_sub['prod_ai']) == set(solution_df['prod_ai']):
        meds_message = "Medications correctly identified!"
    elif len(set(student_sub['prod_ai'])) > len(set(solution_df['prod_ai'])):
        meds_message = 'You\'ved identified more meds than the list in the solution. See the medications tab and compare those in your final data set to the solution list'
    elif len(set(student_sub['prod_ai'])) > len(set(solution_df['prod_ai'])):
        meds_message = 'You\'ved identified fewer meds than the list in the solution. See the medications tab and compare those in your final data set to the solution list'
    else:
        meds_message = 'You\'ve identified some meds incorrectly and/or omitted some in comparison to the solution list. See the medications tab and compare those in your final data set to the solution list'
        
    if index_bool == True:
        index_note = 'In your notebok, when exporting your data, you specified the option (index=True) or otherwise did not change the default behavior of the to_excel() function. This is okay! But you should be aware of the option and the difference between data imported with and without the reatined index'
        output_list = [student_sub.shape[0], student_sub.shape[1], index_note, meds_message]
    else:
        output_list = [student_sub.shape[0], student_sub.shape[1], '', meds_message]
    return(output_list) 
    
    
# Creating a solutions vector     
correct_list = [solution_df.shape[0], solution_df.shape[1], '']


# and initializing a data frame to export 
output_df = pd.DataFrame({'Row Names':['Number of Rows', 'Number of Columns', 'Index Note', 'Medication Note'],
                          'Solution Characteristics':[solution_df.shape[0], solution_df.shape[1], '', '']})

# Checking Python submission
if os.path.isfile(filepath + python_sub_fp):
    print('Python submission file found! Checking solution...')
    py_sln_check = solution_check(filepath + python_sub_fp)
    output_df['Python'] = py_sln_check
else:
    print('No Python submission file found')
    
# Checking R submission
if os.path.isfile(filepath + R_sub_fp):
    print('R submission file found! Checking solution...')
    R_sln_check = solution_check(filepath + R_sub_fp)
    output_df['R'] = R_sln_check 
else:
    print('No R submission file found')

# Checking a general submission    
# Checking R submission
if os.path.isfile(filepath + general_sub_fp):
    print('Suubmission file found wthout "_Python" or "_R" suffix. Checking solution...')
    general_sln_check = solution_check(filepath + general_sub_fp)
    output_df['General'] = general_sln_check 

print('Exporting results to current working directory (wherever you\'ve saved this notebook), Solution_Check_Output.xlsx')

with pd.ExcelWriter(filepath + 'Solution_Check_Output.xlsx') as writer:
    output_df.to_excel(writer, 'CheckResults', index = False)
    pd.DataFrame(set(solution_df['prod_ai'])).to_excel(writer, "Medication List", index=False)
