---
title: "Python Open Education Resource: Analogous R \"Solution\""
subtitle: "Use Case: FDA Adverse Event Reporting Data Aggregation"
date: "Updated: December 22nd, 2020" 
output: 
  html_document:
    number_sections: no
    toc: yes
    keep_md: true
    toc_float:
      collapsed: no
      smooth_scroll: yes
      toc_depth: 3
---





# Preface  
  
For full information related to the University of Pittsburgh's Python Open Education Resource (OER) curation, simulated data, and didactic use cases (such as this one), please visit our [GitHub Repository](https://github.com/domdisanto/Python_OER/). This repository focuses on Python education but contains relevant background information to this use case. 
  
This document was generated in [R](https://cran.rstudio.com/), using the [RStudio IDE](https://rstudio.com/products/rstudio/download/) and [`knitr` package/engine](https://yihui.org/knitr/) and assumes the user is comfortable with working within RStudio and able to knit their R code (although knitting HTML and/or PDF documents is not required or assessed in any of these documents). These documents will also assume a user has a base familiarity in R that includes calling of packages using `library`, some basic syntactical elements in R (such as `<-` to create objects, the classes of objects within R, creating functions in R, etc.). For the sake of clarity, functions taken from specific packages will be called explicitly so that students can know the source package for each function (using R's generic `package::function` syntax). This is however unnecessary analytically. In presenting table output in the final markdown document (most commonly from `... %>% head()` function calls), I include the additional function `... %>% knitr::kable()`, which simply produces more visually appealing tables in HTML. This is not necessary when working within RStudio or for the generation of tables and is completely an aesthetic choice for presenting tables in the rendered document. 
  
A small but important note is that this code heavily utilizes the pipe operator (`%>%`) from the `magrittr` package. This operator is ubiquitous in modern R code and extremely useful to understand (and useful in this document for presenting much more legible code for your review). A wonderful summary is available in Hadley Wickham's and Garret Grolemund's [R for Data Science book (specifically this linked section on the Pipe operator).](https://r4ds.had.co.nz/pipes.html)
  
Lastly, R code will most often utilize the [`tidyverse` family of R packages](https://www.tidyverse.org/). These packages are useful wrapper functions that greatly streamline data cleaning and visualization, which will be conducted specifically using the `ggplot2` package's family of functions. 

  
These documents ***will*** walk you through a solution pathway to the present use case. These documents ***will*** provide example R code to accomplish tasks with relevant annotations to sufficiently describe the purpose of and the code to accomplish each task. This code ***will not*** explicitly teach you R step-by-step or necessarily present all solutions. This code is also ***not*** necessarily formatted organized as may be most suitable/efficient for analysis but rather for education. You are heavily encouraged to pick/take any code or tips from this document and integrate them into a workflow that works best for the purposes of your work!


  
# Introduction

The below document includes code and descriptive text evaluating the use case assessment title here. Full materials for this use case can be found on the Python OER GitHub Repository. This walkthrough document is tentatively titled a "solution" as, while this document offers a specific way of cleaning and analyzing the available, this document certainly does not offer a unique (or even a uniquely-best) solution to the given assessment.

The writing in this document will do its best to outline specific parameters that should be met to satisfactorically complete the assessment. These parameters, tasks, outputs, etc. exist solely to assess your developing skills as an analyst and Python programmer. That being said, if you take different steps or follow a different analytic method to reach the same results, that is perfectly acceptable! This walk through is intended only to be a demonstrated workflow, but it is possible (and even likely) that you may write more efficient, simpler, or more scalable code than what is included here that achieves the same results!

\newpage 

## (0) Loading libraries (akin to Python modules)

This work will only require the `dplyr` package for some minor data frame manipulation. Otherwise, all functions are present in base R without any additional packages installed! 


```r
require(dplyr)
```

## (1) Accessing FAERS Data

Before delving into the programmatic solution, we will outline the brief process to access the FAERS data and specifically the drug-related information of interest. The FAERS Data is located on the FDA's website at https://www.fda.gov/drugs/questions-and-answers-fdas-adverse-event-reporting-system-faers/fda-adverse-event-reporting-system-faers-latest-quarterly-data-files:

<center>
![](C:/Users/Dominic DiSanto/Documents/Python_OER/Use Cases/FAERS_DataPull/R/Images/Fig1_FAERSHeader.jpg)
</center>


This page contains the following link: 

<center>

![Link](C:/Users/Dominic DiSanto/Documents/Python_OER/Use Cases/FAERS_DataPull/R/Images/Fig2_DataAccessButton.jpg)
</center> 
  
which contains quarterly FAERS data more specifically at https://www.fda.gov/drugs/questions-and-answers-fdas-adverse-event-reporting-system-faers/fda-adverse-event-reporting-system-faers-latest-quarterly-data-files.

<center>
![Header](C:/Users/Dominic DiSanto/Documents/Python_OER/Use Cases/FAERS_DataPull/R/Images/Fig3_FAERSDataHEader.jpg)  
</center>


On this page, the data can be accessed by the calendar year in the interface toward the bottom of the page:

<center>
![AnnualData](C:/Users/Dominic DiSanto/Documents/Python_OER/Use Cases/FAERS_DataPull/R/Images/Fig4_DataAnnuals.JPG)  
</center>

Here you can download the data in ASCII (that is text-delimited files) or XML files. The ASCII files are used in the solution below, and are likely the easier data format to use rather than the XML files. I would encourage you to download at least one of the date ranges of data and examine the unzipped files. The folder will a PDF `ReadMe` document that details the files contained. 

In the unzipped folder will also be the data contained in `.txt` files. Data in `.txt` files seems odd right? These are just small text files that would contain written notes from our Notepad app, right? These text files actually contain [text delimited](https://en.wikipedia.org/wiki/Delimiter-separated_values#:~:text=A%20delimited%20text%20file%20is,fields%20separated%20by%20the%20delimiter) data. For example, `.csv` files are actually text-delimited files, where different values in a row are separated by commas. Try opening a `.csv` file on your laptop in Notepad and examine the data. You'll notice data that would open in Excel as:

|Column_1|Column_2|Column_3|...|Column_N|
|--------|--------|--------|---|--------|
|Value_11|Value12|Value_13|...|Value_1N|
|Value_21|Value22|Value_23|...|Value_2N|


would be represented in its text format as:

>Column_1,Column_2,Column_3,...,Column_N  
>Value_11,Value12,Value_13,...,Value_1N  
>Value_21,Value22,Value_23,...,Value_2N  

Try opening one of the smaller (in file-size) `.txt` files from the FAERS data in Notepad or a similar text editor. We see this file is not delimited by commas but dollar-signs ("$"). The next section will work with importing the `.txt` files from the ASCII folder's unzipped files and show you how to work with this new delimiter. Specifically, this only requires the `DRUGS` file as noted below. 


## (2) Importing 2020 Q3 Data

The prompt asks us to aggregate the phenytoin events over the 2019 fiscal year (which we'll call FY2019 for brevity). The definition of the fiscal year is the first fold in this work! In the federal government, the fiscal year most commonly ends on 9/30 (so FY2019 ranges from 10/1/2018 to 9/30/2019). If you've worked in different state agencies, private companies, or other organizations with [various definitions](https://en.wikipedia.org/wiki/Fiscal_year#United_States) of fiscal year end. The import thing for this assignment is to use a *justifiale definition of fiscal year* based on your previous experience, knowledge, or a quick Google search to find. 

We'll begin with a "manually" importing and exploring of the data for Q3 2020, specifically looking at the text file (`.txt`) of drug events. We can import the data file in two ways. The first involves simply importing the data from wherever we have locally saved the data:


```r
filepath <- "C:/Users/Dominic DiSanto/Documents/Python_OER/Use Cases/FAERS_DataPull/ASCII/DRUG20Q3.txt" 
# You would set the above string to the filepath on your local machine to manually import the data, or could simply pass the string in palce of the file path object in the `read.delim` below:
manual_q32020_df <- read.delim(filepath, sep="$", header=T)

# And let's quickly preview some of the rows and a subset of the variables
manual_q32020_df %>% select(1:6) %>% head() %>% knitr::kable()
```



| primaryid|   caseid| drug_seq|role_cod |drugname              |prod_ai              |
|---------:|--------:|--------:|:--------|:---------------------|:--------------------|
| 100046943| 10004694|        1|PS       |LIPITOR               |ATORVASTATIN CALCIUM |
| 100046943| 10004694|        2|SS       |LIPITOR               |ATORVASTATIN CALCIUM |
| 100046943| 10004694|        3|SS       |ATORVASTATIN CALCIUM. |ATORVASTATIN CALCIUM |
| 100046943| 10004694|        4|SS       |ATORVASTATIN CALCIUM. |ATORVASTATIN CALCIUM |
| 100046943| 10004694|        5|C        |SIMVASTATIN.          |SIMVASTATIN          |
| 100048208| 10004820|        1|PS       |DILANTIN              |PHENYTOIN            |


The above chunk relies on a local download of the relevant data to import into R. We would also need to download the other three quarters of data of interest, so it may be somewhat annoying to download all of these files. And if we want to share this code with a new user, each import of the data is going to include the path in our local machine. Since this data is publicly hosted, we can simply use the FDA's hosted zip file to call the data using a stable URL! Below, we import the zipped file as a temporary file:



```r
temp <- tempfile()
download.file("https://fis.fda.gov/content/Exports/faers_ascii_2020Q3.zip", temp)
files_unzip <- unzip(temp)
```

We can then look at the unzipped contents of the zipped folder we called from the FDA's website:


```r
files_unzip
```

```
##  [1] "./ASCII/ASC_NTS.pdf"               "./ASCII/demo20q3.pdf"             
##  [3] "./ASCII/DEMO20Q3.txt"              "./ASCII/drug20q3.pdf"             
##  [5] "./ASCII/DRUG20Q3.txt"              "./ASCII/indi20q3.pdf"             
##  [7] "./ASCII/INDI20Q3.txt"              "./ASCII/outc20q3.pdf"             
##  [9] "./ASCII/OUTC20Q3.txt"              "./ASCII/reac20q3.pdf"             
## [11] "./ASCII/REAC20Q3.txt"              "./ASCII/rpsr20q3.pdf"             
## [13] "./ASCII/RPSR20Q3.txt"              "./ASCII/ther20q3.pdf"             
## [15] "./ASCII/THER20Q3.txt"              "./Deleted/ADR20Q3DeletedCases.txt"
## [17] "./FAQs.pdf"                        "./Readme.pdf"
```

We know we are interestd in the file containing the drug name for the adverse events, and we are specifically interested in the `.txt` files. We can manually call this file:


```r
files_unzip[5]
```

```
## [1] "./ASCII/DRUG20Q3.txt"
```

or we could use the regular expression search `grep` function that is built into R to identify the string that includes `DRUG` and `txt` in the file name, identifying the name of the data file we'd like to import! 


```r
# File names that include "DRUG"
grep("DRUG", files_unzip, ignore.case = T, value = T)
```

```
## [1] "./ASCII/drug20q3.pdf" "./ASCII/DRUG20Q3.txt"
```

```r
# File names that include "txt"
grep("txt", files_unzip, ignore.case = T, value = T)
```

```
## [1] "./ASCII/DEMO20Q3.txt"              "./ASCII/DRUG20Q3.txt"             
## [3] "./ASCII/INDI20Q3.txt"              "./ASCII/OUTC20Q3.txt"             
## [5] "./ASCII/REAC20Q3.txt"              "./ASCII/RPSR20Q3.txt"             
## [7] "./ASCII/THER20Q3.txt"              "./Deleted/ADR20Q3DeletedCases.txt"
```

```r
# File name that include "DRUG" **and** "txt"
files_unzip[files_unzip %in% grep("DRUG", files_unzip, ignore.case = T, value = T) & files_unzip %in% grep("txt", files_unzip, ignore.case = T, value = T)]
```

```
## [1] "./ASCII/DRUG20Q3.txt"
```


So let's supply the file-name of interest to our `read.delim()` function, and explore the imported dataset.

```r
drug_txt_file <- files_unzip[files_unzip %in% grep("DRUG", files_unzip, ignore.case = T, value = T) & files_unzip %in% grep("txt", files_unzip, ignore.case = T, value = T)]

drug_df <- read.delim(drug_txt_file, sep="$", header=T)

drug_df %>% nrow()
```

```
## [1] 1895153
```

```r
drug_df %>% select(1:6) %>% head() %>% knitr::kable()
```



| primaryid|   caseid| drug_seq|role_cod |drugname              |prod_ai              |
|---------:|--------:|--------:|:--------|:---------------------|:--------------------|
| 100046943| 10004694|        1|PS       |LIPITOR               |ATORVASTATIN CALCIUM |
| 100046943| 10004694|        2|SS       |LIPITOR               |ATORVASTATIN CALCIUM |
| 100046943| 10004694|        3|SS       |ATORVASTATIN CALCIUM. |ATORVASTATIN CALCIUM |
| 100046943| 10004694|        4|SS       |ATORVASTATIN CALCIUM. |ATORVASTATIN CALCIUM |
| 100046943| 10004694|        5|C        |SIMVASTATIN.          |SIMVASTATIN          |
| 100048208| 10004820|        1|PS       |DILANTIN              |PHENYTOIN            |

Now let's see what medications exist in the data, and identify all instances of `phenytoin` in the medications, again using the `grep` function. 


```r
meds <- unique(drug_df$prod_ai)

grep("phenytoin", meds, ignore.case=T, value = T)
```

```
## [1] "PHENYTOIN"                       "PHENYTOIN SODIUM"               
## [3] "FOSPHENYTOIN SODIUM"             "FOSPHENYTOIN"                   
## [5] "PHENOBARBITAL\\PHENYTOIN SODIUM"
```

And lastly let's filter the full imported data set using our identifying adverse events related to phenytoin. 


```r
phenytoin_q3 <- drug_df %>% filter(prod_ai %in% grep("phenytoin", unique(drug_df$prod_ai), ignore.case=T, value = T))

phenytoin_q3 %>% nrow()
```

```
## [1] 1620
```

```r
phenytoin_q3 %>% select(1:6) %>% head() %>% knitr::kable()
```



|  primaryid|   caseid| drug_seq|role_cod |drugname          |prod_ai          |
|----------:|--------:|--------:|:--------|:-----------------|:----------------|
|  100048208| 10004820|        1|PS       |DILANTIN          |PHENYTOIN        |
|  100048208| 10004820|        2|SS       |DILANTIN          |PHENYTOIN        |
|  102985303| 10298530|        2|C        |DILANTIN          |PHENYTOIN        |
| 1039375511| 10393755|       39|C        |PHENYTOIN SODIUM. |PHENYTOIN SODIUM |
| 1039375511| 10393755|       41|C        |DILANTIN          |PHENYTOIN        |
|  104988686| 10498868|        1|PS       |PHENYTOIN SODIUM. |PHENYTOIN SODIUM |


## (3) Importing All FY2019 Data 

We walked through the process of importing a singe quarter of data. FY2019 will include four years of data that will follow an analgous process, so let's create a function to reduce the redundancy of our code. The below function requires only the file path of the quarter's zipped folder, and will complete the steps above of importing the full folder, unzipping the data cotents, identifying the `DRUG` file, and specifically filtering on `phenytoin`. The chunk also compares teh results of the function to our above manual input, to demonstrate the function and manual import resulting in the same imported data!  



```r
faers_phenytoin_extract <- function(filepath){
  temp <- tempfile()
  download.file(filepath, temp)
  files_unzip <- unzip(temp)

  drug_txt_file <- files_unzip[files_unzip %in% grep("DRUG", files_unzip, ignore.case = T, value = T) & files_unzip %in% grep("txt", files_unzip, ignore.case = T, value = T)]

  drug_df <- read.delim(drug_txt_file, sep="$", header=T)

  return(drug_df %>% filter(prod_ai %in% grep("phenytoin", unique(drug_df$prod_ai), ignore.case=T, value = T)))

}

q3_20_df <- faers_phenytoin_extract("https://fis.fda.gov/content/Exports/faers_ascii_2020Q3.zip")

all(phenytoin_q3 == q3_20_df, na.rm = T)
```

```
## [1] TRUE
```

```r
# All the same as our manual extract! 
```

Now that we've simplified our code by defining a function and confirmed its accuracy, let's extract the phenytoin data 


```r
q2_20_df <- faers_phenytoin_extract("https://fis.fda.gov/content/Exports/faers_ascii_2020Q2.zip")
q1_20_df <- faers_phenytoin_extract("https://fis.fda.gov/content/Exports/faers_ascii_2020Q1.zip")
q4_19_df <- faers_phenytoin_extract("https://fis.fda.gov/content/Exports/faers_ascii_2019Q4.zip")
```

We want to combine the results of our import, so let's confirm we have the same columns in all of our data sets.

```r
(colnames(q3_20_df) == colnames(q2_20_df)) %>% all()
```

```
## [1] TRUE
```

```r
(colnames(q3_20_df) == colnames(q1_20_df)) %>% all()
```

```
## [1] TRUE
```

```r
(colnames(q3_20_df) == colnames(q4_19_df)) %>% all()
```

```
## [1] TRUE
```

Let's then append the data frames together, and look at our final data


```r
fy19_phenytoin <- rbind(q3_20_df %>% mutate(Year="2020Q3")
                        , q2_20_df %>% mutate(Year="2020Q2")
                        , q1_20_df %>% mutate(Year="2020Q1")
                        , q4_19_df %>% mutate(Year="2019Q4"))


fy19_phenytoin %>% nrow()
```

```
## [1] 5837
```

```r
fy19_phenytoin %>% select(1:6) %>% head() %>% knitr::kable()
```



|  primaryid|   caseid| drug_seq|role_cod |drugname          |prod_ai          |
|----------:|--------:|--------:|:--------|:-----------------|:----------------|
|  100048208| 10004820|        1|PS       |DILANTIN          |PHENYTOIN        |
|  100048208| 10004820|        2|SS       |DILANTIN          |PHENYTOIN        |
|  102985303| 10298530|        2|C        |DILANTIN          |PHENYTOIN        |
| 1039375511| 10393755|       39|C        |PHENYTOIN SODIUM. |PHENYTOIN SODIUM |
| 1039375511| 10393755|       41|C        |DILANTIN          |PHENYTOIN        |
|  104988686| 10498868|        1|PS       |PHENYTOIN SODIUM. |PHENYTOIN SODIUM |


## (4) Exporting aggregated data


```r
write.csv(fy19_phenytoin, "FY2019_PhenytoinAERs.csv", row.names = F)
```

