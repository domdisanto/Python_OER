## Python Open Education Resource
## Python Open Education Resource
### PTSD Use Case
### Student Assessment
### Drafted: 9/8/2020
### Updated: 9/8/2020
>	Dominic DiSanto: Initial drafting of document

> #### Notes:
> 1) PTSD diagnosis can be altered to be severity if we want every patient to "meet" the criteria for PTSD diagnosis
> 2) Need to define a stratification point based on covariates for data cleaning (2)
> 3) The visualization question for (2b) under Data Cleaning can be removed or fleshed out based on desired output of this use case
> 4) I've included PHQ9 based only on my own previous experience, but can always use other SRB measures or simply provide a binary suicidal endorsement variable 


#### Data Cleaning & Exploratory Analysis
1) Create a PTSD diagnosis variable 
   a. See the following links as useful resources to the PTSD checklist and respective variable coding and a guide to the scoring and diagnosis of PTSD using this checklist
   b. What is the prevalence of PTSD in this sample? How does this compare to other estimates of PTSD in military populations? 
2) Stratify the sample on medication information and compare prevalence of PTSD in these two segments of the sample    
   a. Does there appear to be a group with a higher prevalence?
   b. How would you visually convey this information to “non-technical expert”? Create this visual
3) Create suicidality variable
   a. See the following article containing the PHQ9 questions. The 9th question in PHQ9 is often used to assess suicidality, with any values >1 (i.e. present symptom) indicating suicidal endorsement
 
#### Build your model
1) Build a model on the training set predicting 6-month SRB and predicting 6-month PTSD diagnosis using **input features**
2) Assess your model fit
3) Predict the 6-month outcome of observations in the test set
   a) Suppose these predictions are correct, how well do the prescribed medications improve PTSD outcomes if at all? How much or little do they exacerbate SRB symptoms?
   b) Are there cases of predicted onset SRB where none was present at baseline? What changes in PTSD diagnosis/severity are observed in these patients? 
		
