## Python Open Education Resource
## VA Dual Enrollment 
### Student Assessment
### Drafted: 9/7/2020
### Updated: 9/20/2020
 > Dominic DiSanto: Updated to flesh out and provide more detail in the student assessment. Provided references (and uploaded source documents) to this folder. I hope to include screenshots directly in this file, but have been unable to properly load the image even when stored locally in this repository folder. Upon completion of the accompanying "walkthrough" notebook, the exploratory analysis/visualization section will include a figure/visualization to emulate as well, providing additionanl student direction for matplotlib visualization skills (e.g. axis labelling, data preparation, coloring/fill in stacked bar graph, etc.) 

### Background
This assignment 


This use case aims to give you experience relevant in the following areas: \
**Modules:** 1 (Importing/Reading Data); 4 (Pandas Intro); 5 (Relational Data/Data Merging); 6 (Data Cleaning); 7 (Data Visualization) \
**Competencies:** Pandas (general); Data merging; Matplotlib/Visualization (basic, general); Cleaning string data; Cleaning inconsistently coded data   
**Preface Notes & Assumptions:**  
- Assume all `buprenorphine` medications are equivalent to buprenorphine tablets in the given reference table for morphine mg equivalents 

### Steps/Assignment

#### Data Cleaning & Preparation
1) Import CMS and VA data into your Jupyter Notebook
2) Create opioid administration outcome variable of interest within both the VA and CMS data  
    a) *We want to simply capture whether a given patient was given an opioid, essentially whether that patients medication was an opioid or not. What could a variable that codes this information look like?*
3) Standardize coding of relevant variables within data frames *and* between VA and CMS data sources (*Examine units and/or variables that may be included as a singular variable in one data set and as a pair or set of values in a different data set*).  
    a) Dose Value (by daily intake)  
    b) Social Security Number (SSN)  
    c) Medication Duration    
4) Identify total, daily intake of mg morphine equivalents (summing **both** VA and CMS values for dual enrolled patients)  
    a) A PDF of the [Center for Medicare and Medicaid Service's "Conversion Factors" Document](https://www.cms.gov/Medicare/Prescription-Drug-coverage/PrescriptionDrugCovContra/Downloads/Opioid-Morphine-EQ-Conversion-Factors-Aug-2017.pdf) and a screenshot (accessed 9/22/2020) included below for your reference.  
       
![MG Morphine Equiv Chart](https://github.com/domdisanto/Python_OER/blob/master/Use%20Cases/VA%20Dual%20Enrollment%20Case/Instructor%20Materials/Opioid_MorphineMgEquiv.JPG)
  

6) Merge data frames together on common identifier (SSN)  
7) Create and indicator variable to identify individuals dually enrolled in VA and CMS healthcare systems.    
8) Create a **sum** variable for total mg-morphine-equivalents within dual-use patients    
    
    
#### Exploratory Analysis & Visualization
1) How many patients are dual enrolled and how many were solely accessing VA healthcare resources?  
2) Visualize MME among patients using histograms and/or density curves:  
    a) Separately for VA patient visits and CMS patient visits (using only VA and CMS prescriptions respectively)  
    b) For dual-enrollment patients (using our MME total/sum variable created in ***Data Cleaning Step 8***)   
    c) Analyze the comparative visualizations (i.e. differences you do (or do not) see).
3) What proportion of dual enrolled patients were prescribed an opioid? Similarly, what proportion of "VA-only" patients?  
     a) What proportion of dual enrolled patients were prescribed an opioid during both their VA and CMS visits? 
4) Create a visual that illustrates this difference    





#### Example Visualizations

Q4:  
  
![VA MME Histogram](https://github.com/domdisanto/Python_OER/blob/master/Use%20Cases/VA%20Dual%20Enrollment%20Case/Instructor%20Materials/VA_MME_Hist.png)    
  
![CMS MME Histogram](https://github.com/domdisanto/Python_OER/blob/master/Use%20Cases/VA%20Dual%20Enrollment%20Case/Instructor%20Materials/CMS_MME_Hist.png)  
  
![VA MME Density Curve](https://github.com/domdisanto/Python_OER/blob/master/Use%20Cases/VA%20Dual%20Enrollment%20Case/Instructor%20Materials/VA_MME_Dens.png)  
  
![CMS MME Density Curve](https://github.com/domdisanto/Python_OER/blob/master/Use%20Cases/VA%20Dual%20Enrollment%20Case/Instructor%20Materials/CMS_MME_Dens.png)
