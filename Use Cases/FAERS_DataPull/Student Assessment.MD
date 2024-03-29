## Python Open Education Resource
### FAERS Data Aggregation
### Student Assessment
### Drafted: 12/23/2020
### Updated: 12/23/2020
>	Dominic DiSanto: Initialization


#### Competencies  
**Modules**: 1 (Importing/Reading Data); 4 (Pandas Intro); 5 (Relational Data/Data Merging); 6 (Data Cleaning)
**Competencies**: Pandas (general); Data merging


### Introduction & Tasks 

Taken from the [FDA's website](https://www.fda.gov/drugs/surveillance/questions-and-answers-fdas-adverse-event-reporting-system-faers):

> The FDA Adverse Event Reporting System (FAERS) is a database that contains adverse event reports, medication error reports and product quality complaints resulting in adverse events that were submitted to FDA. The database is designed to support the FDA's post-marketing safety surveillance program for drug and therapeutic biologic products.

This use case involves accessing the FAERS data from the FDA's website. We will specifically only be interested in the tables related to the drugs involved in each reported event. We will also limit the assignment to a single medication to reduce the size of the data you will manipulate and export. The FAERS data source is a rich resource of much more information than is explored through this use case, and you're encouraged to examine the data outside of the task presented below!   


### Tasks

Access the FDA's Adverse Events Reporting System Data (FAERS) data, and pull all drug events related to Phenytoin from the data's `DRUGS` files for fiscal year 2019 (or FY2019). Aggregate FY2019 data into a single `xlsx` data file titlted `FY2019_Phenytoin_FAERS_Python.xlsx` or `FY2019_Phenytoin_FAERS_R.xlsx` for each respective program. Please leave all columns/variables in the data set, only filtering rows/observations for adverse drug events related to Phenytoin. 

This data is publicily accessible, such that you can download and import the files from a local folder. As the data are publicily hosted, the [following StackOverflow post](https://stackoverflow.com/questions/23419322/download-a-zip-file-and-extract-it-in-memory-using-python3) may be useful to review to attempt extracting data directly from the FDA's website using the `zipfile`, `requests`, and `io` Python modules. 

The included Python script `FAERS_SolutionCheck.py` will check your supplied solutions for accuracy, by simply running the code:
> `exec(open(AERS_SolutionCheck.py).read())`

in your Jupyter notebook.

*The presented task for this assignment is intentionally very vague. The walkthrough Jupyter notebook and RMarkdown documents will discuss both the programmatic solution with coding examples and the data access for the FAERS data. You're encourage to do your best to download, explore, access, etc. the data on your own as much as possible to create the final aggregate data set.*
