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


#### Data Cleaning & Exploratory Analysis
1) Import patient outcome data. How many patients that you identified in question 1 have available outcome data? How many were not recruited or have missing follow-up data (i.e. are not in this outcome data set)?


2) Create a binary PTSD diagnosis/outcome variable. The following links include useful resources [the PTSD checklist and respective variable coding](https://www.ptsd.va.gov/professional/assessment/documents/PCL5_Standard_form.PDF) and [a guide to the scoring and diagnosis of PTSD using this checklist](https://www.ptsd.va.gov/professional/assessment/adult-sr/ptsd-checklist.asp#obtain), with relevant information included below in Figures 1A and 1B     
  
|Figure 1A|Figure 1B|
|---------|---------|
| ![Checklist](https://github.com/domdisanto/Python_OER/blob/master/Use%20Cases/PTSD%20%26%20SRB%20Use%20Case/Instructor%20Materials/Fig/PTSD_Checklist_vars.JPG)| ![Diagnostic Criteria](https://github.com/domdisanto/Python_OER/blob/master/Use%20Cases/PTSD%20%26%20SRB%20Use%20Case/Instructor%20Materials/Fig/PTSD_Diagnosis_Criteria.png) |  
  
a) What is the baseline prevalence of PTSD in this sample? How does this compare to other estimates of PTSD in military populations? (*You do nto need to exhaustively research PTSD. Simply use [Google Scholar](http://scholar.google.com/) or [PubMed](https://www.ncbi.nlm.nih.gov/pubmed) to find an article or two, possibly a review article, that estimates PTSD prevalence in military populations*).   

3) Create a variable that identifies suicidal ideation as present or absent      
     a) See [the following article](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1495268/#app1) containing the PHQ9 questions. The 9th question in PHQ9 is often used to assess suicidality, with any values >1 (i.e. present symptom) indicating suicidal endorsement/ideation and is contained in your data set. 

4) Now import the patient medication data. What is the dimensionality? How any rows are included and how many unique patients?   
     a) Identify for each patient whether or not a PTSD treatment was prescribed using the indication variable "Treatment/Indication" column

#### Build your model
1) Build a model on the training set predicting 6-month SRB and predicting 6-month PTSD diagnosis using input features of age, years of military service, combat exposure during deployment, alcohol abuse, AFQT score, income category, and self-reported perceived social support score.
2) Assess the fit of both your models  
3) Identify "important" features within your predictive models of PTSD and SRB. 
     a) How do you define/assess "importance"?
     b) What features are important in predicting both PTSD ***and*** SRB? 
     c) What is the relationship of the features you identified in **3b** to each of the outcomes? Do these characteristics present as possible "protective" or "risk" factors overall? 
4) What type of model did you fit and what specific measure did you use in ***3a*** to assess importance? List two other types of classification models and how you would assess feature importance for these different models. 
