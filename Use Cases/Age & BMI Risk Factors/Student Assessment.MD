## Python Open Education Resource

## Joint Assignment (Excel - Python - R )

### BMI Use case

### Student Assessment

#### Drafted: 12/13/20

#### Updated: 12/29/20

> Added detail to background 

### Introduction

In this use case, you are given a list of patients (designated by a random patient identifier variable) and their measured heights (in centimeters) and weight (in kilograms) seen by your clinic over the past week. You've been tasked with identifying a number of patients who are at risk for cardiovascular complications that will be specifically noted for additional follow-up. You must identify these patients based on the supplied criteria and compile their contact information.

*Acknowledgement: Patient contact information simulated using the [`Faker` Python module](https://faker.readthedocs.io/en/master/)*

### Competencies  
**Modules**: 1 (Importing/Reading Data); 4 (Pandas Intro); 5 (Relational Data/Data Merging); 6 (Data Cleaning) 
**Competencies**: Pandas (general); Data merging; Data reading/importing and writing/exporting 

### Solution Formatting

The following information may be useful to know *prior* to beginning work on this assessment. 

A workbook is included in this folder titled `BMI_Solution_Excel.xlsx`. This file contains one method of solving the tasks in Excel from the instructors. This workbook may be a useful reference for the Excel solution for the `vlookup` formulae contained in the solution sheets. The file also demonstrates the final format that your solutions must follow to be checked by the Python script detailed below.

In an attempt to more easily allow you to check your solutions, this use case contains a Python script (`automate_data_check_bmi.py`) that will check your answers. Use of this script is not required, but simply supplied for your convenience. If you would not like to use this script, feel free to use the manual solutions supplied. 

For the script to check your solutions:
- The columns in your solutions dataframes must be only include (and be named correctly) `ID`, `PhoneNo`, and `Address`
- Your solution spreadsheets must be `.xlsx` files named `BMI_Solution_Python`, `BMI_Solution_Excel`, `BMI_Solution_R`, and `BMI_Solution_Update` with the tabs `Criteria_1`, `Criteria_2`, `Criteria_3`, and `Criteria_4` 
- In supplying your answers using Excel, the submitted data must contain *only* those observations meeting the criteria, and not simply a list of all observations filtered for the criteria. 


The script can be run most easily by simply downloading and saving the `.py` script in the same folder as your solution files, original data, and solution notebook, and run the following line of code in a chunk:
> `exec(open('automate_data_check_bmi.py').read())`

The script will export a spreadsheet (`.xlsx`) file titled `SolutionCheckResults.xlsx`, with tabs for the Excel, Python, R, and "Update" solution spreadsheets you've created.  The script works even in the absence of these scripts, so you can run the scripts to check your answer to any one of your solutions without having created all four files.


## Tasks

1) Working solely in Excel, calculate BMI for all patients, rounding the value to the hundredths. Create four tabs of patient ID's and contact information for patients that meet the following criteria. Save the spreadsheet of your four solution tabs as `BMI_Solution_Excel.xlsx.` The use of `vlookup()` or `xlookup` may be helpful!
     a) BMI$\geq$30
     b) BMI$\geq$35
     c) BMI$\geq$30 and Age$\geq$60
     d) BMI$\geq$35 and Age$\geq$60

2) Now, using Python, import the height & weight data and the contact information from the `BMI_Data.xlsx` spreadsheet's tabs. Calculate BMI using the formula $BMI = \frac{Weight (kg)}{Height (m)^2}$ and **round to the hundredths (`np.round(..., 2)`)**. *Note the height value that you're supplied is given in centimeters*.

3) Repeat step 2 using R

4) You've now been supplied an updated patient list in the data set `BMI_Data_UPDATE.xlsx`. Using the same 4 criteria (and instrutions noted in the **Solutions** section), identify the patient contact information for patients in this updated data set using your preferred method in R, Python, or Excel. 
