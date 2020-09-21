## Python Open Education Resource
## VA Dual Enrollment 
### Student Assessment
### Drafted: 9/7/2020
### Updated: 9/7/2020
 > Dominic DiSanto: Initial drafting of document (and upload to GitHub)

#### Background



### Steps/Assignment

#### Data Cleaning & Preparation
1) Import CMS and VA data into your Jupyter Notebook
2) Create opioid administration outcome variable of interest within both the VA and CMS data
3) Standardize coding of relevant variables between VA and CMS data sources (*Examine units and/or variables that may be included as a singular variable in one data set and as a pair or set of values in a different data set*).
    a) Height
    b) Weight
    c) Dose Value (by daily intake)
    d) Social Security Number (SSN)
3) Merge data frames together on common identifier (SSN)
4) Identify individuals dually enrolled in VA and CMS healthcare systems 

5) Identify total, daily intake of mg morphine equivalents 
6) Consider the sum of intake for patients that are "dually enrolled" 
     a) The below screenshot is taken from the [Center for Medicare and Medicaid Service's "Conversion Factors" Document](https://www.cms.gov/Medicare/Prescription-Drug-coverage/PrescriptionDrugCovContra/Downloads/Opioid-Morphine-EQ-Conversion-Factors-Aug-2017.pdf) for your reference. This PDF was accessed on 9/21/2020 and uploaded to this same folder for your reference as well. 
![Alt text](Instructor Materials/Opioid_MorphineMgEquiv.jpg?raw=true "title")


#### Exploratory Analysis & Visualization
1) Compare rates of outcomes by those dual-enrolled and those enrolled in only the VA healthcare system
2) Create visual to demonstrate differences in outcomes between two classes of patients


<i>Outside of this basic visualization and data management, do we want to have students build a model? Could easily identify how important the dual enrollment feature is to mortality? Maybe it would be interesting to show the protective effect of dual enrollment BUT when overprescribed (which is more likely when dual enrolled), patients are extremely more at risk for overdose mortality and all-cause mortality. Importance of communication between healthcare systems</i>
