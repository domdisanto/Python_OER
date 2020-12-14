"""
BMI Use Case Check Script
Written: 12/12/2020
Updated: 12/12/2020
@author: Dominic DiSanto
"""

#!/usr/bin/env python3


import pandas as pd
import numpy as np

def sln_check(submission, solution, num, correct, note):
    
    submission_cln =  submission.sort_values('ID').reset_index(drop=True)    
    submission_cln = submission_cln[~np.isnan(submission_cln['ID'])]
    
    solution_cln =  solution.sort_values('ID').reset_index(drop=True)    
    solution_cln = solution_cln[~np.isnan(solution_cln['ID'])]
    
    xmax = max(submission_cln.shape[0], solution_cln.shape[0])
    ymax = max(submission_cln.shape[1], solution_cln.shape[1])

    bool_check = 0

    for j in ['ID', 'PhoneNo', 'Address']:
        for i in range(xmax):
            bool_check = bool_check + (solution_cln.loc[i, j] == submission_cln.loc[i, j])

    if bool_check == xmax*ymax:
        correct[num] = 'Correct!'
        note[num] = ''
    elif solution_cln.shape[0] != submission_cln.shape[0]:
        correct[num] = 'Some errors present, see note'
        note[num] = 'Unequal number of rows (i.e. observations). Some patients incorrectly included and/or some incorrectly excluded'
    elif solution.shape[1] != submission_cln.shape[1]:
        correct[num] = 'Some errors present, see note'
        note[num] = 'Unequal number of columns. Ensure your answer contains only patient ID, phone number, and address'
    else:
        correct[num] = 'Some errors present, see note'
        note[num] = 'Correct dimensions supplied (i.e. correct number of rows and columns), but some correct observations erroneously excluded as well as incorret patients included'


# Initial Data Set

## Importing Data and Creating Answer Key/Solutions
sln_hw = pd.read_excel('BMI_Data.xlsx', sheet_name = 'HeightWeight')
sln_ctc = pd.read_excel('BMI_Data.xlsx', sheet_name = 'Contact Info')

sln_hw['BMI'] = np.round(sln_hw['Weight (kg)'] / (sln_hw['Height (cm)']/100)**2, 2)
sln_hw

sln1 = pd.merge(sln_hw.loc[sln_hw['BMI']>=30, 'ID'], sln_ctc, on='ID')
sln1 = sln1.sort_values('ID')

sln2 = pd.merge(sln_hw.loc[sln_hw['BMI']>=35, 'ID'], sln_ctc, on='ID')
sln2 = sln2.sort_values('ID')

sln3 = pd.merge(sln_hw.loc[(sln_hw['BMI']>=30) & (sln_hw['Age']>=60), 'ID'], sln_ctc, on='ID')
sln3 = sln3.sort_values('ID')

sln4 = pd.merge(sln_hw.loc[(sln_hw['BMI']>=35) & (sln_hw['Age']>=60), 'ID'], sln_ctc, on='ID')
sln4 = sln4.sort_values('ID')


## Excel Submission
correct_xcl = [[], [], [], []]
note_xcl = [[], [], [], []]

### Criteria 1
try:
    excel_sln1 = pd.read_excel('BMI_Solution_Excel.xlsx', sheet_name='Criteria_1')
    sln_check(sln1, excel_sln1, 0, correct_xcl, note_xcl)
except:
    note_xcl[0] = 'Error importing file, please check your submission. If you feel this is an error, please contact the instructors via GitHub and consult the manual submission key for feedback in the interim'   

### Criteria 2 
try:    
    excel_sln2 = pd.read_excel('BMI_Solution_Excel.xlsx', sheet_name='Criteria_2')
    sln_check(sln2, excel_sln2, 1, correct_xcl, note_xcl)
except:
    note_xcl[1] = 'Error importing file, please check your submission. If you feel this is an error, please contact the instructors via GitHub and consult the manual submission key for feedback in the interim'   

### Criteria 3
try:    
    excel_sln3 = pd.read_excel('BMI_Solution_Excel.xlsx', sheet_name='Criteria_3')
    sln_check(sln3, excel_sln3, 2, correct_xcl, note_xcl)
except:
    note_xcl[2] = 'Error importing file, please check your submission. If you feel this is an error, please contact the instructors via GitHub and consult the manual submission key for feedback in the interim'   

### Criteria 4
try:    
    excel_sln4 = pd.read_excel('BMI_Solution_Excel.xlsx', sheet_name='Criteria_4')
    sln_check(sln4, excel_sln4, 3, correct_xcl, note_xcl)
except:
    note_xcl[3] = 'Error importing file, please check your submission. If you feel this is an error, please contact the instructors via GitHub and consult the manual submission key for feedback in the interim'   

    
excel_df = pd.DataFrame({'Criteria':list(range(1, 5)),
                            'Correct':correct_xcl,
                            'Feedback':note_xcl})
    

    
## Python Submission
correct_python = [[], [], [], []]
note_python = [[], [], [], []]

### Criteria 1
try:
    python_sln1 = pd.read_excel('BMI_Solution_Python.xlsx', sheet_name='Criteria_1')   
    sln_check(sln1, python_sln1, 0, correct_python, note_python)
except:
    note_python[0] = 'Error importing file, please check your submission. If you feel this is an error, please contact the instructors via GitHub and consult the manual submission key for feedback in the interim'   

### Criteria 2
try:     
    python_sln2 = pd.read_excel('BMI_Solution_Python.xlsx', sheet_name='Criteria_2')
    sln_check(sln2, python_sln2, 1, correct_python, note_python)
except:
    note_python[1] = 'Error importing file, please check your submission. If you feel this is an error, please contact the instructors via GitHub and consult the manual submission key for feedback in the interim'   

### Criteria 3
try:    
    python_sln3 = pd.read_excel('BMI_Solution_Python.xlsx', sheet_name='Criteria_3')
    sln_check(sln3, python_sln3, 2, correct_python, note_python)
except:
    note_python[2] = 'Error importing file, please check your submission. If you feel this is an error, please contact the instructors via GitHub and consult the manual submission key for feedback in the interim'   

### Criteria 4
try:    
    python_sln4 = pd.read_excel('BMI_Solution_Python.xlsx', sheet_name='Criteria_4')
    sln_check(sln4, python_sln4, 3, correct_python, note_python)
except:
    note_python[3] = 'Error importing file, please check your submission. If you feel this is an error, please contact the instructors via GitHub and consult the manual submission key for feedback in the interim'   

    
python_df = pd.DataFrame({'Criteria':list(range(1, 5)),
                            'Correct':correct_python,
                            'Feedback':note_python})  
    
## R Submission
correct_R= [[], [], [], []]
note_R= [[], [], [], []]

try:
    ### Criteria 1
    R_sln1 = pd.read_excel('BMI_Solution_R.xlsx', sheet_name='Criteria_1')
    R_sln1 = R_sln1[~np.isnan(R_sln1['ID'])]
    R_sln1 = R_sln1.sort_values('ID')
    
    sln_check(sln1, R_sln1, 0, correct_R, note_R)
except:
    note_R[0] = 'Error importing file, please check your submission. If you feel this is an error, please contact the instructors via GitHub and consult the manual submission key for feedback in the interim'   

try:    
    ### Criteria 2 
    R_sln2 = pd.read_excel('BMI_Solution_R.xlsx', sheet_name='Criteria_2')
    R_sln2 = R_sln2[~np.isnan(R_sln2['ID'])]
    
    sln_check(sln2, R_sln2, 1, correct_R, note_R)
except:
    note_R[1] = 'Error importing file, please check your submission. If you feel this is an error, please contact the instructors via GitHub and consult the manual submission key for feedback in the interim'   

try:    
    ### Criteria 3
    R_sln3 = pd.read_excel('BMI_Solution_R.xlsx', sheet_name='Criteria_3')
    R_sln3  = R_sln3[~np.isnan(R_sln3['ID'])]
    
    sln_check(sln3, R_sln3, 2, correct_R, note_R)
except:
    note_R[2] = 'Error importing file, please check your submission. If you feel this is an error, please contact the instructors via GitHub and consult the manual submission key for feedback in the interim'   

try:    
    ### Criteria 4
    R_sln4 = pd.read_excel('BMI_Solution_R.xlsx', sheet_name='Criteria_4')
    R_sln4 = R_sln4[~np.isnan(R_sln4['ID'])]
   
    sln_check(sln4, R_sln4, 3, correct_R, note_R)
except:
    note_R[3] = 'Error importing file, please check your submission. If you feel this is an error, please contact the instructors via GitHub and consult the manual submission key for feedback in the interim'   

    
R_df = pd.DataFrame({'Criteria':list(range(1, 5)),
                            'Correct':correct_R,
                            'Feedback':note_R})  
    
# Updated Data Submission Check
    
## Importing Data and Creating Answer Key/Solutions
sln_upd_hw = pd.read_excel('BMI_Data_UPDATE.xlsx', sheet_name = 'HeightWeight')
sln_upd_ctc = pd.read_excel('BMI_Data_UPDATE.xlsx', sheet_name = 'Contact Info')

sln_upd_hw['BMI'] = np.round(sln_upd_hw['Weight (kg)'] / (sln_upd_hw['Height (cm)']/100)**2, 2)
sln_upd_hw

sln_upd_1 = pd.merge(sln_upd_hw.loc[sln_upd_hw['BMI']>=30, 'ID'], sln_upd_ctc, on='ID')
sln_upd_1 = sln_upd_1.sort_values('ID')

sln_upd_2 = pd.merge(sln_upd_hw.loc[sln_upd_hw['BMI']>=35, 'ID'], sln_upd_ctc, on='ID')
sln_upd_2 = sln_upd_2.sort_values('ID')

sln_upd_3 = pd.merge(sln_upd_hw.loc[(sln_upd_hw['BMI']>=30) & (sln_upd_hw['Age']>=60), 'ID'], sln_upd_ctc, on='ID')
sln_upd_3 = sln_upd_3.sort_values('ID')

sln_upd_4 = pd.merge(sln_upd_hw.loc[(sln_upd_hw['BMI']>=35) & (sln_upd_hw['Age']>=60), 'ID'], sln_upd_ctc, on='ID')
sln_upd_4 = sln_upd_4.sort_values('ID')

## Creating submission check data frame
correct_update = [[], [], [], []]
note_update = [[], [], [], []]

### Criteria 1
try:
    update_sln1 = pd.read_excel('BMI_Solution_UPDATE.xlsx', sheet_name='Criteria_1')
    sln_check(sln_upd_1, update_sln1, 0, correct_update, note_update)
except:
    note_update[0] = 'Error importing file, please check your submission. If you feel this is an error, please contact the instructors via GitHub and consult the manual submission key for feedback in the interim'   

### Criteria 2 
try:    
    update_sln2 = pd.read_excel('BMI_Solution_UPDATE.xlsx', sheet_name='Criteria_2')
    sln_check(sln_upd_2, update_sln2, 1, correct_update, note_update)
except:
    note_update[1] = 'Error importing file, please check your submission. If you feel this is an error, please contact the instructors via GitHub and consult the manual submission key for feedback in the interim'   

### Criteria 3
try:    
    update_sln3 = pd.read_excel('BMI_Solution_UPDATE.xlsx', sheet_name='Criteria_3')
    sln_check(sln_upd_3, update_sln3, 2, correct_update, note_update)
except:
    note_update[2] = 'Error importing file, please check your submission. If you feel this is an error, please contact the instructors via GitHub and consult the manual submission key for feedback in the interim'   

### Criteria 4
try:    
    update_sln4 = pd.read_excel('BMI_Solution_UPDATE.xlsx', sheet_name='Criteria_4')
    sln_check(sln_upd_4, update_sln4, 3, correct_update, note_update)
except:
    note_update[3] = 'Error importing file, please check your submission. If you feel this is an error, please contact the instructors via GitHub and consult the manual submission key for feedback in the interim'   

    
update_df = pd.DataFrame({'Criteria':list(range(1, 5)),
                            'Correct':correct_update,
                            'Feedback':note_update})
    
with pd.ExcelWriter('SolutionCheckResults.xlsx') as writer:
    excel_df.to_excel(excel_writer = writer,
                    sheet_name = "Excel Submission", 
                    index = False)
    python_df.to_excel(excel_writer = writer,
                    sheet_name = "Python Submission", 
                    index = False)
    R_df.to_excel(excel_writer = writer,
                    sheet_name = "R Submission", 
                    index = False)
    update_df.to_excel(excel_writer = writer,
                       sheet_name = "Updated Data Submission",
                       index=False)