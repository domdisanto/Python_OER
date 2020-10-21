## Management & Maintenance Notes

### Updated: 10/20/2020

> #### Update: Updated document with removed future directions/next steps from student assessment document


Currently, the PTSD data most notably differs from Will & Noah's presentation by not using any ICD-9 or ICD10 diagnosis code data to identify PTSD but the checklist/lLikert scale variables thT I've generated. I've "separated" the medication data, such that there is merging required. 

If in the future we want this use case to directly fllow Noah and Will's presentation, the initial steps (both for data sim and student assessment) can be edited to have a larger cohort of patents with no PTSD checklist but rather an ICD diagnosis code (9, 10, or a mix). 

The only reason for the difference between the current use case from Noah and Will's is to distance the competencies covered in this use case to prioritize sklearn and model fitting over the pandas/numpy data cleaning covered previously in the VA dual use case, but these data cleaning steps could certainly be included in this use case. 


> #### Notes:
> 1) PTSD diagnosis can be altered to be severity if we want every patient to "meet" the criteria for PTSD diagnosis
> 3) The visualization question for (2b) under Data Cleaning can be removed or fleshed out based on desired output of this use case
> 4) I've included PHQ9 based only on my own previous experience, but can always use other SRB measures or simply provide a binary suicidal endorsement variable 
> 5) Can also flesh out details on modelling (force students to use k-fold CV or a specific model) or leave it open-ended and leave students to their own devices


