## Management & Maintenance Notes
### Updated: 10/19/2020

> #### Update Notes: Expanded on possibly future directions (which aren't necessary so not considered pending but could be used to further develop the use case) related to using the dates/times of medication administration, an improved use of the medications data that would require cleaning of the "messy" strings, and the idea of building in a mortality status outcome for supervised learning. 


### Medication Data
In the data simulation, I purposefully varied the syntax/spelling/case etc, of the medications to complicate working with the medication data. In the assessment prompts and solution, there is no true need to standardize medications across the two data sets (VA and CMS). Students can simply work with the complete list of medications, accounting for typos, case differences, etc. This is "okay"; students get experience with annoyances of string data in having to identify all of the different ways a medication is presented. But a future direction could take this further by "forcing" students to standardize medication. Below are some of my proposals:  
    1. A simple frequency question: "How often is each opioid medication assigned at VA visits? CMS visits?"  
    2. A further dive into dual-use patients: "Among dual-enrolled patients, how many patients were prescribed *the same opioid* from their VA and CMS visits?"  
    3. Further work could include a relationship that patients who are dual-enrolled opioids are at high risk for mortality, and patients dual-prescribed *the same opioid* are at an even further elevated risk. 



### Date/Time Information
Currently do not utilize the time-date information, but could further complicate/build out this use case by emulating Dr. Gellad's (30 day overlap) task. This would be not only asking students to identify patients who were dual prescribed opioids or over prescribed using MME, but to further assess how many days of overprescription each patient experienced using the prescription length and the date of visit variables. 


### Mortality Status Outcome
Students would then have to identify and could build simple classification models to predict mortality status. The goal would be to have mortality reduced for patients who are dual enrolled but **who do not** receive multiple opioid prescriptions, but significantly elevated for those with dual prescriptions and those with 120+ mg morphine equivalents. The take-home being that dual-enrollment of healthcare can be a positive when the systems communicate and reduce risks of over-prescription.



  
