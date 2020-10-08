## Python Open Education Resource
## VA Dual Enrollment 
### Student Assessment
### Drafted: 9/7/2020
### Updated: 10/07/2020
 > Dominic DiSanto: Updated to flesh out and provide more detail in the student assessment. Provided references (and uploaded source documents) to this folder. I hope to include screenshots directly in this file, but have been unable to properly load the image even when stored locally in this repository folder. Upon completion of the accompanying "walkthrough" notebook, the exploratory analysis/visualization section will include a figure/visualization to emulate as well, providing additionanl student direction for matplotlib visualization skills (e.g. axis labelling, data preparation, coloring/fill in stacked bar graph, etc.) 

### Background  
This use cases borrows from both a [publication](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6219924/) and [Presentation](https://www.hsrd.research.va.gov/for_researchers/cyber_seminars/archives/video_archive.cfm?SessionID=3543)  by Dr. Walid Gellad within Pittsburgh's Veterans Affairs Hospital system. The simulated data emulates a simplified set of prescription data for Veterans Affairs (VA) and Center for Medicaid/Medicare Services (CMS) patients, with overlap of healthcare utiliation in both systems. 
  
This use case aims to give you experience relevant in the following areas: \
**Modules:** 1 (Importing/Reading Data); 4 (Pandas Intro); 5 (Relational Data/Data Merging); 6 (Data Cleaning); 7 (Data Visualization) \
**Competencies:** Pandas (general); Data merging; Matplotlib/Visualization (basic, general); Cleaning string data; Cleaning inconsistently coded data   
**Preface Notes & Assumptions:**  
- Assume all `buprenorphine` medications are equivalent to buprenorphine tablets in the given reference table for morphine mg equivalents 

### Steps/Assignment

#### Data Cleaning & Preparation
1) Import CMS and VA data into your Jupyter Notebook
    a) Examine the data. Are the variables consistently names between the two data frames? Is the same information collected? What differences exist? 
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


#### Bonus Questions

The below questions demonstrate additional skills that, while beyond the scope of building foundational Python competencies/skills, may be of interest to explore if you found the earlier assessment simple!

1) Create a density plot of total mg morphine equivalents among dual-enrolled patients, among VA-only patients, and among CMS only patients. Shade in the plot for patients with greater-than-or-equal-to 120 mg morphine equivalents   
     a) *Hint: [This StackOverflow post](https://stackoverflow.com/questions/39666591/how-to-extract-x-y-data-from-kdensity-plot-from-matplotlib-for-python) may be useful in extracting densities using `scipy`)*


#### Example Visualizations  
  
Below are example visualizations or "solution" to check your work for the assessment. The results are hidden by default, but simply click each header to expand the corresponding section where you can compare to your visualizations (or to give you a specific visual to recreate if you're unsure where to start)!
   
<details>  
<summary> Proportion of Dual Enrollment (Q1) </summary>
In total, there are 808 patients, 424 VA-only patients and 384 CMS patients. All of the CMS patients are contained within the VA data, so we also have 384 dual-enrolled patients. 

![Dual Enrollment Bar](https://github.com/domdisanto/Python_OER/blob/master/Use%20Cases/VA%20Dual%20Enrollment%20Case/Instructor%20Materials/Dual_Enrollment_bar.png)  
</details>  

  
<details>
<summary>EDA & Visualization Q2:</summary>    
 
![CMS MME Density](https://github.com/domdisanto/Python_OER/blob/master/Use%20Cases/VA%20Dual%20Enrollment%20Case/Instructor%20Materials/CMS_MME_Dens.png)
![CMS MME Histogram](https://github.com/domdisanto/Python_OER/blob/master/Use%20Cases/VA%20Dual%20Enrollment%20Case/Instructor%20Materials/CMS_MME_Hist.png)  
![VA MME Density](https://github.com/domdisanto/Python_OER/blob/master/Use%20Cases/VA%20Dual%20Enrollment%20Case/Instructor%20Materials/VA_MME_Dens.png)
![VA MME Histogram](https://github.com/domdisanto/Python_OER/blob/master/Use%20Cases/VA%20Dual%20Enrollment%20Case/Instructor%20Materials/VA_MME_Hist.png)    
![Dual MME Density](https://github.com/domdisanto/Python_OER/blob/master/Use%20Cases/VA%20Dual%20Enrollment%20Case/Instructor%20Materials/Dual_MME_Dens.png)
![Dual MME Histogram](https://github.com/domdisanto/Python_OER/blob/master/Use%20Cases/VA%20Dual%20Enrollment%20Case/Instructor%20Materials/Dual_MME_Hist.png)  
</details>


<details>  
<summary> Proportion of Dual Enrollment (Q1) </summary>
Of 424 total "VA-only" patients, 157, (37.03%) were prescribed an opioid by their respective VA hospital.      <br>
Of 384 total "CMS-only" patients, 196, (51.04%) were prescribed an opioid by their CMS hospital visit.     <br>
Of 384 total dually-enrolled patients, 274, (71.35%) were prescribed an opioid by either the VA *or* CMS healthcare systems.    <br>
Of 384 total dually-enrolled patients, 79, (20.57%) were prescribed an opioid by either the VA *or* CMS healthcare systems.   <br>
</details>  

<details>  
<summary> Visualization of Opioid Prescriptions (Q4)  </summary>
Included are some example, summary visualiations for Question 4, but the question is deliberately left open-ended, so your visualizations may not mirror teh format or structure (or possibly even contain different information) than those presented below. Proper visualizations should include a descriptive title, label axes, sufficiently be able to present information with little-to-no additional description/contextualization.     
   
A last note, there is nothing "incorrect" about plotting frequencies when comparing our patient populations. However as we are most interested in comparing differences in "rates", proportions/percentages convey a more apt comparison than do simple frequency/count data.  

![Opioid Proportion (1)](https://github.com/domdisanto/Python_OER/blob/master/Use%20Cases/VA%20Dual%20Enrollment%20Case/Instructor%20Materials/q4_opioid_viz1.png)  
![Opioid Proportion (2)](https://github.com/domdisanto/Python_OER/blob/master/Use%20Cases/VA%20Dual%20Enrollment%20Case/Instructor%20Materials/q4_opioid_viz2.png)  
</details>

<details>
<summary> Bonus Visualization</summary> 
 
![VA Bonus Shade Density](https://github.com/domdisanto/Python_OER/blob/master/Use%20Cases/VA%20Dual%20Enrollment%20Case/Instructor%20Materials/VA_bonusviz.png)
![Dual Bonus Shade Density](https://github.com/domdisanto/Python_OER/blob/master/Use%20Cases/VA%20Dual%20Enrollment%20Case/Instructor%20Materials/dual_bonusviz.png)
![CMS Bonus Shade Density](https://github.com/domdisanto/Python_OER/blob/master/Use%20Cases/VA%20Dual%20Enrollment%20Case/Instructor%20Materials/CMS_bonusviz.png)
</details>
