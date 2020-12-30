/*********************
Python OER
PTSD Use Case
SQL "Solution"

Preface:
     Only working through tasks in the Student Assessment pertinent to SQL:
	 (1) Identify patients with PTSD diagnoses in the ICD data (with ICD-9, ICD-10 the codes of 309.81, F43.10, F43.11, F43.12)
	 (2) Create a binary PTSD diagnosis/outcome variable in the research cohort 
	 (3) Create a variable that categorizes suicial ideation as absent or present in the research cohort 
	 (4) Examine other datasets in the table in the research cohort 
**********************/

/* (1) Identify patients with PTSD diagnoses in the ICD data (with ICD-9, ICD-10 the codes of 309.81, F43.10, F43.11, F43.12) */

-- Always useful to first examine your data
	SELECT TOP 10 * 
	FROM PythonOER.[dbo].[PossiblePTSDPatients_ICD]

-- Now looking at the diagnosis codes of interest
	SELECT PatientID
	       , ICDCode
		   , Age
	FROM PythonOER.[dbo].[PossiblePTSDPatients_ICD]
	WHERE ICDCode IN ('309.81', 'F43.10', 'F43.11', 'F43.12')
	AND Age>=18 -- 514

-- Notice we have some duplicated Patient ID's
	SELECT PatientID
	       , ICDCode
		   , Age
	FROM PythonOER.[dbo].[PossiblePTSDPatients_ICD]
	WHERE ICDCode IN ('309.81', 'F43.10', 'F43.11', 'F43.12') 
	AND AGE>=18
	AND PatientID IN(
		SELECT PatientID
		FROM PythonOER.[dbo].[PossiblePTSDPatients_ICD]
		WHERE ICDCode IN ('309.81', 'F43.10', 'F43.11', 'F43.12')
		GROUP BY PatientID
		HAVING COUNT(*)>1
		)

-- To get a correct number of patients, we will identify distint PatientID's with relevant diagnoses 
SELECT COUNT(*) FROM (
	SELECT DISTINCT PatientID
	FROM PythonOER.[dbo].[PossiblePTSDPatients_ICD]
	WHERE ICDCode IN ('309.81', 'F43.10', 'F43.11', 'F43.12')
	AND Age>=18
) AS A -- 456

SELECT COUNT(*) FROM (
	SELECT PatientID
	FROM PythonOER.[dbo].[PossiblePTSDPatients_ICD]
	WHERE ICDCode IN ('309.81', 'F43.10', 'F43.11', 'F43.12')
	GROUP BY PatientID
) AS A -- 456


/* Now working with the Patient Research data in PTSD_ResearchCohort */

/* (2) Create a binary PTSD diagnosis/outcome variable in the research cohort  */

-- Always useful to examine our data!
SELECT TOP 10 * 
FROM PythonOER.dbo.PTSD_ResearchCohort

-- Using the assigned PTSD criteria, creating a 6-month PTSD binary diagnosis variable 

DROP TABLE IF EXISTS #tmpPTSD -- Very useful line to include when creating/working with temporary tables

SELECT CASE WHEN 
         (PTSD_Q1_6mo>1 OR PTSD_Q2_6mo>1 OR PTSD_Q3_6mo>1 OR PTSD_Q4_6mo>1 OR PTSD_Q5_6mo>1) 
		 AND
		 (PTSD_Q6_6mo>1 OR PTSD_Q7_6mo>1) 
		 AND 
		 (PTSD_Q8_6mo>1 OR PTSD_Q9_6mo>1 OR PTSD_Q10_6mo>1 OR PTSD_Q11_6mo>1 OR PTSD_Q12_6mo>1 OR PTSD_Q13_6mo>1 OR PTSD_Q14_6mo>1)
		 AND
		 (PTSD_Q15_6mo>1 OR PTSD_Q16_6mo>1 OR PTSD_Q17_6mo>1 OR PTSD_Q18_6mo>1 OR PTSD_Q19_6mo>1 OR PTSD_Q20_6mo>1) THEN 1
		 ELSE 0 END AS PTSD_6mo
		 , * -- Retaining all other variables
INTO #tmpPTSD -- Storing the results in a new, temporary table that we can easily exaine/access
FROM PythonOER.dbo.PTSD_ResearchCohort

	-- Examining the results
	SELECT TOP 10 * 
	FROM #tmpPTSD 

	-- Seeing the prevalence of PTSD using our diagnostic criteria
	SELECT PTSD_6mo
	       , COUNT(*) -- COUNT(*) to examine frequencies of 
	FROM #tmpPTSD 
	GROUP BY PTSD_6mo -- Grouping by our PTSD diagnosis variable, so we simply get counts of distinct values for this PTSD field

/* (3) Create a variable that categorizes suicial ideation as absent or present in the research cohort  */
-- A much simpler task simply using the PHQ question we are provided

DROP TABLE IF EXISTS #tmpSRB

SELECT CASE WHEN PHQ_Q9_6mo>0 THEN 1 
       ELSE 0 END AS SRB_6mo
	   , *
INTO #tmpSRB
FROM #tmpPTSD -- Using our previous temporary table, but you could also use the original data as FROM PythonOER>dbo.PTSD_ResearchCohort


	-- Examining the results
	SELECT TOP 10 * 
	FROM #tmpSRB

	-- Checking prevalence of SRB in our cohort
	SELECT SRB_6mo
	       , COUNT(*) 
	FROM #tmpSRB
	GROUP BY SRB_6mo

	-- And prevalence of SRB & PTSD 
	SELECT PTSD_6mo
	       , SRB_6mo
		   , COUNT(*) 
	FROM #tmpSRB
	GROUP BY SRB_6mo, PTSD_6mo


/* (4) Examine other datasets in the table in the research cohort */

-- In SQL, our data exploration capabilities are limited compred to analytic languages like Python, R
-- However we can examine some central tendencies/basic characteristics of our data

-- We'll look at the continuous variables first 

	-- AGE 
	DROP TABLE IF EXISTS #tmpAgeSummary

	SELECT ROUND(AVG(AGE), 2) AS Age_Mean-- Mean/Average
	       , ROUND(STDEV(AGE), 2) AS Age_StDev -- Standard Deviation
		   , MIN(AGE) AS Age_Min
		   , MAX(Age) AS Age_Max
		   , CAST(MIN(AGE) AS nvarchar) + '-' + CAST(MAX(AGE) AS nvarchar) AS Age_Range
		   , COUNT(DISTINCT AGE) AS Age_DistinctValsN
	INTO #tmpAgeSummary
	FROM PythonOER.dbo.PTSD_ResearchCohort	
	
	SELECT * 
	FROM #tmpAgeSummary

	-- Social Support
	DROP TABLE IF EXISTS #tmpSocial

	SELECT ROUND(AVG(SocialSupport), 2) AS SocialSupport_Mean-- Mean/Average
	       , ROUND(STDEV(SocialSupport), 2) AS SocialSupport_StDev -- Standard Deviation
		   , MIN(SocialSupport) AS Social_Min
		   , MAX(SocialSupport) AS Social_Max
		   , CAST(MIN(SocialSupport) AS nvarchar) + '-' + CAST(MAX(SocialSupport) AS nvarchar) AS Social_Range
		   , COUNT(DISTINCT SocialSupport) AS Social_DistinctValsN
	INTO #tmpSocial
	FROM PythonOER.dbo.PTSD_ResearchCohort	
	
	SELECT * 
	FROM #tmpSocial

	-- Time to diagnosis 
	DROP TABLE IF EXISTS #tmpDiagnosis

	SELECT ROUND(AVG(TimeFirstDiagnosis_Months), 2) AS Diagnosis_Mean-- Mean/Average
	       , ROUND(STDEV(TimeFirstDiagnosis_Months), 2) AS Diagnosis_StDev -- Standard Deviation
		   , MIN(TimeFirstDiagnosis_Months) AS Diagnosis_Min
		   , MAX(TimeFirstDiagnosis_Months) AS Diagnosis_Max
		   , CAST(MIN(TimeFirstDiagnosis_Months) AS nvarchar) + '-' + CAST(MAX(TimeFirstDiagnosis_Months) AS nvarchar) AS Diagnosis_Range
		   , COUNT(DISTINCT TimeFirstDiagnosis_Months) AS Diagnosis_DistinctValsN
	INTO #tmpDiagnosis
	FROM PythonOER.dbo.PTSD_ResearchCohort	
	
	SELECT * 
	FROM #tmpDiagnosis

	-- Beck Anxiety Inventory 
	DROP TABLE IF EXISTS #tmpBeck

	SELECT ROUND(AVG(BeckAnxiety_BL), 2) AS Beck_Mean-- Mean/Average
	       , ROUND(STDEV(BeckAnxiety_BL), 2) AS Beck_StDev -- Standard Deviation
		   , MIN(BeckAnxiety_BL) AS Beck_Min
		   , MAX(BeckAnxiety_BL) AS Beck_Max
		   , CAST(MIN(BeckAnxiety_BL) AS nvarchar) + '-' + CAST(MAX(BeckAnxiety_BL) AS nvarchar) AS Beck_Range
		   , COUNT(DISTINCT BeckAnxiety_BL) AS Beck_DistinctValsN
	INTO #tmpBeck
	FROM PythonOER.dbo.PTSD_ResearchCohort	
	
	SELECT * 
	FROM #tmpBeck


	-- Since we've created a number of temporary tables, we can even aggregate the results 
	SELECT 'Age' AS VarName
	       , Age_Mean AS Mean -- Renaming variables in the first table so they are not variable specific
		   , Age_StDev AS StdDev
		   , Age_Min AS Min
		   , Age_Max AS Max
		   , Age_Range AS Range
		   , Age_DistinctValsN AS DistinctValsN
	FROM #tmpAgeSummary
	UNION -- Appends two tables with the same number of columns
	SELECT 'SocialSupport' AS VarName, *
	FROM #tmpSocial
	UNION -- Appends two tables with the same number of columns
	SELECT 'Time to Diagnosis' AS VarName, *
	FROM #tmpDiagnosis
	UNION
	SELECT 'Beck Anxiety Inventory' AS VarName, *
	FROM #tmpBeck



-- Lastly we can look at the categorical frequency of some of our discrete variables

	-- Alcohol Abuse
	SELECT AlcAbuse, COUNT(*) AS Freq
	FROM PythonOER.dbo.PTSD_ResearchCohort
	GROUP BY AlcAbuse

	-- Income Category
	SELECT IncomeCat, COUNT(*) AS Freq
	FROM PythonOER.dbo.PTSD_ResearchCohort
	GROUP BY IncomeCat

	-- Medications
	SELECT PTSD_Rx, COUNT(*) AS Freq
	FROM PythonOER.dbo.PTSD_ResearchCohort
	GROUP BY PTSD_Rx

--  And as an example, we can create indicator varibles for each Income Category group, as an example of creating dummy variables 
	-- We will just explore these results, but not store them in a full table

SELECT TOP 100 IncomeCat 
       , CASE WHEN IncomeCat = '<125% FPL' THEN 1 ELSE 0 END AS IncomeCat_125less
	   , CASE WHEN IncomeCat = '125%-200% FPL' THEN 1 ELSE 0 END AS IncomeCat_125_200
	   , CASE WHEN IncomeCat = '200%-400% FPL' THEN 1 ELSE 0 END AS IncomeCat_200_400
	   , CASE WHEN IncomeCat = '400%+ FPL' THEN 1 ELSE 0 END AS IncomeCat_400more
FROM PythonOER.dbo.PTSD_ResearchCohort


-- Recall we can also count cross-tabulations (i.e. categorical frequency among many categorical variables) using the GROUP BY clause
	SELECT IncomeCat
	       , PTSD_6mo
		   , COUNT(*) AS Freq
	FROM #tmpPTSD
	GROUP BY IncomeCat, PTSD_6mo

	-- Or even 3 variables (although the results are a little hard to decipher)
	SELECT IncomeCat
	       , PTSD_6mo
		   , SRB_6mo
		   , COUNT(*) AS Freq
	FROM #tmpSRB
	GROUP BY IncomeCat, PTSD_6mo, SRB_6mo

