## Python Open Education Resource
### PTSD Use Case
### Student Assessment
### Drafted: 9/8/2020
### Updated: 10/19/2020
>	Dominic DiSanto: Updates along initial data simulation, clarification of questions based on data elements resulting structure in data sim.


#### Data Cleaning & Exploratory Analysis
1) Create a PTSD diagnosis variable   
     a) The following links include useful resources [the PTSD checklist and respective variable coding](https://www.ptsd.va.gov/professional/assessment/documents/PCL5_Standard_form.PDF) and [a guide to the scoring and diagnosis of PTSD using this checklist](https://www.ptsd.va.gov/professional/assessment/adult-sr/ptsd-checklist.asp#obtain), with relevant information included below in Figures 1A and 1B     
  
|Figure 1A|Figure 1B|
|---------|---------|
| ![Checklist](https://github.com/domdisanto/Python_OER/blob/master/Use%20Cases/PTSD%20%26%20SRB%20Use%20Case/Instructor%20Materials/Fig/PTSD_Checklist_vars.JPG)| ![Diagnostic Criteria](https://github.com/domdisanto/Python_OER/blob/master/Use%20Cases/PTSD%20%26%20SRB%20Use%20Case/Instructor%20Materials/Fig/PTSD_Diagnosis_Criteria.png) |  
  
  b. What is the baseline prevalence of PTSD in this sample? How does this compare to other estimates of PTSD in military populations? (*You do nto need to exhaustively research PTSD. Simply use [Google Scholar](http://scholar.google.com/) or [PubMed](https://www.ncbi.nlm.nih.gov/pubmed) to find an article or two, possibly a review article, that estimates PTSD prevalence in military populations*).   

2) Create a variable that identifies suicidal ideation as present or absent      
     a) See [the following article](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1495268/#app1) containing the PHQ9 questions. The 9th question in PHQ9 is often used to assess suicidality, with any values >1 (i.e. present symptom) indicating suicidal endorsement/ideation and is contained in your data set. 


2) Stratify the sample on medication information and compare prevalence of PTSD in these two segments of the sample   
     a) Does there appear to be a group with a higher prevalence?   
     b) How would you visually convey this information to “non-technical expert”? Create this visual   
  
#### Build your model
1) Build a model on the training set predicting 6-month SRB and predicting 6-month PTSD diagnosis using input features of age, years of military service, combat exposure during deployment, alcohol abuse, AFQT score, income category, and self-reported perceived social support score.
2) Assess the fit of both your models  
3) Identify "important" features within your predictive models of PTSD and SRB. 
     a) How do you define/assess "importance"?
     b) What features are important in predicting both PTSD ***and*** SRB? 
     c) What is the relationship of the features you identified in **3b** to each of the outcomes? Do these characteristics present as possible "protective" or "risk" factors overall? 
4) What type of model did you fit and what specific measure did you use in ***3a*** to assess importance? List two other types of classification models and how you would assess feature importance for these different models. 
