## Python Open Education Resource
### PTSD Use Case
### Student Assessment
### Drafted: 9/8/2020
### Updated: 10/19/2020
>	Dominic DiSanto: Updates along initial data simulation, clarification of questions based on data elements resulting structure in data sim.

### Introduction

The present use case uses a simulated data set of patients with PTSD and suicidal-ideation or suicidal-related behavior (SRB) outcome data. This data and use case are inspired by the work of Noah Delapaz and William Hor under Dr. Lirong Wang related to pharmaceutical treatment of PTSD and related, adverse suicidal ideation. In this use case, you will first be given a large list of patients and previous ICD-9 and ICD-10 diagnoses, within which you will identify a patient sample of interest with a diagnosis of PTSD (as if you were identifying a study sample in the early stages of a research project).   
  
After identifying your study sample of interest, you will use patient outcome and medication data to assess the effects of common PTSD-treatments on later diagnosis of PTSD and/or SRB. Steps will include data cleaning, exploratory data analysis, and model-building and evaluation as you work with this use case.


#### Competencies  
**Modules**: 1 (Importing/Reading Data); 4 (Pandas Intro); 5 (Relational Data/Data Merging); 6 (Data Cleaning); Assorted Classification Modules   
**Competencies**: Pandas (general); Data merging; Matplotlib/Visualization (basic, general); Cleaning string data; Cleaning inconsistently coded data; Sci-kit learn; Model fitting and cross-validation; Various possible classification model algorithms

#### "Cohort Identification"

1) The dataset `PossiblePatients_ICD.csv` contains a list of ~1,000 patients from a hypothetical electronic health record registry with various ICD-9 and ICD-10 diagnosis codes. We want to identify adult patients (18+) with a diagnosis of post-traumatic stress disorder. We will use the codes of `309.81`, `F43.10`, `F43.11`, `F43.12` to identify our diagnosis of interest. How many patients do you find in this data set that are eligible for your research study (i.e that meet this criteria)?


#### Data Cleaning & Exploratory Analysis

Now we will work with the file `PTSD_ResearchCohort.csv`, a dataset of the 401 patients who were recruited and successfully completed our hypothetical study. A data dictionary is included below for reference:

<details>
  <summary> Data Dictionary </summary>  
  
|*Variable*|*Description*|
|---|---|
|`PTSD_Q1`-`PTSD_Q20`|PTSD Questionnaire variables (see images below) describing presence of symptoms 6-months after study enrollment|
|`PHQ_Q9`|Patient Health Questionnaire (or PHQ-9) question 9, which assessed presence of suicidality or ideation of suicide, also at 6-months after study enrollment|
|`Age`|"Continuous" (integer) age variable|
|`TimeFirstDiagnosis_Months`| Integer value. The number of months since the patient's first diagnosis of PTSD|
|`AlcAbuse`|Binary variable, where 1 represents present alcohol abuse and 0 no alcohol abuse over the previous 6 months|
|`BeckAnxiety_BL`|Continuous measure ranging from 0-63, where higher values indicate greater presence and severity of anxiety symptoms|
|`IncomeCat`|Nominal categorical varible describing income category relative to the federal poverty line (described in the variable's categories)|
|`SocialSupport`|Self-reported ["social support"](https://www.tnaap.org/documents/mspss-multidimensional-scale-of-perceived-social.pdf), with values ranging from 0 to 84, where higher values indicate higher self-reported social support |
|`PTSD_Rx`|Name of medication prescribed|
</details>

1) Import the research study data. We can assume that the patients in this data file are a sbuset of the eligible patients you identified above. How many patients that you identified in question 1 have available outcome data? How many were not recruited or have missing follow-up data (i.e. are not in this outcome data set)?


2) Using the PTSD questionnaire vairiables, crate a binary PTSD diagnosis/outcome variable. The following links include useful resources [the PTSD checklist and respective variable coding](https://www.ptsd.va.gov/professional/assessment/documents/PCL5_Standard_form.PDF) and [a guide to the scoring and diagnosis of PTSD using this checklist](https://www.ptsd.va.gov/professional/assessment/adult-sr/ptsd-checklist.asp#obtain), with relevant information included below in Figures 1A and 1B.     
  
|Figure 1A|Figure 1B|
|---------|---------|
| ![Checklist](https://github.com/domdisanto/Python_OER/blob/master/Use%20Cases/PTSD%20%26%20SRB%20Use%20Case/Instructor%20Materials/Fig/PTSD_Checklist_vars.JPG)| ![Diagnostic Criteria](https://github.com/domdisanto/Python_OER/blob/master/Use%20Cases/PTSD%20%26%20SRB%20Use%20Case/Instructor%20Materials/Fig/PTSD_Diagnosis_Criteria.png) |  
   

3) Create a variable that identifies suicidal ideation as present or absent:      
     a) See [the following article](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1495268/#app1) as a reference describing the PHQ9 questions. The 9th question in PHQ9 is often used to assess suicidality, with any values >1 (i.e. present symptom) indicating suicidal endorsement/ideation and is contained in your data set. 

4) Beyond the PTSD & PHQ variables, examine the other variables in the data set, and their descriptions in the Data Dictionary above. For any categorical variables, create indicator/dummy variables. 

#### Build your model
1) Build a model on the training set predicting 6-month SRB and predicting 6-month PTSD diagnosis using the input features dentified in the data dictionary and that you've prepared in the data cleaning section above of age, time since earliest PTSD diagnosis, alcohol abuse, Beck Anxiety Inventory, alcohol abuse, income category, social support, and medication indicator variables. **Select a modelling algorithm that allows you to examine feature importance. **
2) Assess the fit of both your models  
3) What medications are "important" in a predictive model of PTSD? Describe the relationship of each medication (generally) based on the level of evidence (say "high" or "low") based on your interpretation of the results of your model. 

4) What type of model did you fit and what specific measure did you use in ***3a*** to assess importance? List two other types of classification models and how you would assess feature "importance" for these different models. 


#### Bonus Questions

1) Included in the `Instructor Materials` folder are two data sets, `icd9codes.csv` and `icd10codes.xlsx`, that contain all unique ICD-9 and ICD-10 codes respectively and brief text descriptions of the diseases represented by each code. Using the text descriptions in these two datasets, identify the ICD-9 and ICD-10 codes corresponding to diagnoses of post-traumatic stress disorder. Your results should yield the four codes used as "case-definitions" of PTSD in the first, **"Cohort Identification"** question.  
     *Hint:* Try the [str.contains](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.contains.html) function.
