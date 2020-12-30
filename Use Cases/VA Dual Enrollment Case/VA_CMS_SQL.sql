/*********************
Python OER
VA-CMS Dual Enrollment Use Case
SQL "Solution"

Preface:
     Only working through tasks in the Student Assessment pertinent to SQL:
	 (1) "Import" (not really) and examine the data
	 (2) Create opioid administration variable in VA and CMS tables 
	 (3) Standardize coding of relevant variables between VA aned CMS tables
	 (4) Identify total of morphine mg equivalents (MME's) 
	 (5) Merge together VA & CMS data frames
	 (6) Create and indicator variable to identify individuals dually enrolled in VA and CMS healthcare systems.
	 (7) Create a sum variable for total mg-morphine-equivalents within dual-use patients

**********************/

-- (1) "Import" (not really) and examine the data
SELECT TOP 10 * 
FROM PythonOER.dbo.CMS_Data

SELECT TOP 10 * 
FROM PythonOER.dbo.VA_Data


-- (2) Create opioid administration variable in VA and CMS tables 

-- First examining the unique medications in each data 
	SELECT DISTINCT Medication
	FROM PythonOER.dbo.VA_Data
	
	SELECT DISTINCT Medication
	FROM PythonOEr.dbo.CMS_Data

-- We will work with the data "as-is" (as referenced in the Jupyter notebook solution)
  -- VA
	DROP TABLE IF EXISTS #tmpVA_opioid

	SELECT *
	       , CASE WHEN Medication IN ('BUPERNORPHINE', 'BUPRENORPHINE', 'BUPRENORPHINE TABLET', 'BUTORPHANOL', 'DIHYDROCODEINE',
                                      'TRAMADOL', 'buprenorphine', 'bupernorphine', 'butorphanol', 'dihydrocodeine', 'tramadol',
                                      'tramadol HCL', 'dihydrocodeine-acetaminophin-caff') 
			 THEN 1 ELSE 0 END AS Opioid
	INTO #tmpVA_opioid
	FROM PythonOER.dbo.VA_Data

	SELECT TOP 100 Medication
	               , Opioid
	FROM #tmpVA_opioid

  -- CMS
  	DROP TABLE IF EXISTS #tmpCMS_opioid

	SELECT *
	       , CASE WHEN Medication IN ('BUPERNORPHINE', 'BUPRENORPHINE', 'BUPRENORPHINE TABLET', 'BUTORPHANOL', 'DIHYDROCODEINE',
                                      'TRAMADOL', 'buprenorphine', 'bupernorphine', 'butorphanol', 'dihydrocodeine', 'tramadol',
                                      'tramadol HCL', 'dihydrocodeine-acetaminophin-caff') 
			 THEN 1 ELSE 0 END AS Opioid
	INTO #tmpCMS_opioid
	FROM PythonOER.dbo.CMS_Data

	SELECT TOP 100 Medication
	               , Opioid
	FROM #tmpCMS_opioid





-- (3) Standardize coding of relevant variables between VA aned CMS tables
	-- (a) Dose Value
	-- (b) Social Security Number (SSN, our identifier) 
	-- (c) Medication Duration

-- (a) Dose Value
	-- VA
	SELECT DISTINCT Medication_Dose_Unit
	FROM PythonOER.dbo.VA_Data

	DROP TABLE IF EXISTS #tmpVA_dose

	SELECT CASE WHEN Medication_Dose_Unit = 'mg' THEN Medication_Dose
	       WHEN Medication_Dose_Unit = 'mcg' THEN Medication_Dose / 1000 END AS Dose_Recalc
		   , *
	INTO #tmpVA_dose
	FROM #tmpVA_opioid

	SELECT Medication_Dose_Unit, Medication_Dose, Dose_Recalc
	FROM #tmpVA_Dose

	--CMS
	SELECT DISTINCT Medication_Dose_Unit
	FROM PythonOER.dbo.CMS_Data

	DROP TABLE IF EXISTS #tmpCMS_dose

	SELECT CASE WHEN Medication_Dose_Unit = 'mg' THEN Medication_Dose
	       WHEN Medication_Dose_Unit = 'mcg' THEN Medication_Dose / 1000 END AS Dose_Recalc
		   , *
	INTO #tmpCMS_dose
	FROM #tmpCMS_opioid

	SELECT Medication_Dose_Unit, Medication_Dose, Dose_Recalc
	FROM #tmpCMS_Dose



-- (b) Social Security Number
	-- VA
	SELECT TOP 10 Patient_ID
	FROM PythonOER.dbo.VA_Data
		-- We will leave the VA data as is (numeric only, essentially an integer)

	-- CMS
	DROP TABLE IF EXISTS #tmpCMS_ID

	SELECT TOP 10 Patient_ID
	FROM #tmpCMS_Dose
	
	SELECT REPLACE(Patient_ID, '-', '') AS Patient_ID_Edit
	       , *
	INTO #tmpCMS_ID
	FROM #tmpCMS_Dose

	SELECT TOP 50 Patient_ID_Edit
	       , Patient_ID
	FROM #tmpCMS_ID


-- (c) Medication Duration
	-- VA
	SELECT DISTINCT Medication_Duration_Unit -- Examining unique categories of units
	FROM #tmpVA_dose

	SELECT TOP 10 Medication_Duration_Unit, Medication_Duration_Value -- Quickly exploring units & values 
	FROM #tmpVA_Dose

	DROP TABLE IF EXISTS #tmpVA_duration

	SELECT *
	       , CASE WHEN Medication_Duration_Unit = 'Day' THEN Medication_Duration_Value  
		     WHEN Medication_Duration_Unit = 'Week' THEN Medication_Duration_Value*7
			WHEN Medication_Duration_Unit = 'Month' THEN Medication_Duration_Value*30
			END AS Duration_Recalc
	INTO #tmpVA_duration
	FROM #tmpVA_dose

	SELECT TOP 100 Medication_Duration_Unit
	              , Medication_Duration_Value
				  , Duration_Recalc
	FROM #tmpVA_duration

	-- CMS
	SELECT DISTINCT Duration_Unit -- Examining unique categories of units 
	FROM #tmpCMS_ID

	SELECT TOP 10 Duration_Unit, Medication_Duration -- Quickly exploring units & values  
	FROM #tmpCMS_ID

	DROP TABLE IF EXISTS #tmpCMS_duration

	SELECT *
	       , CASE WHEN Duration_Unit = 'Day' THEN Medication_Duration  
		     WHEN Duration_Unit = 'Week' THEN Medication_Duration*7
			WHEN Duration_Unit = 'Month' THEN Medication_Duration*30
			END AS Duration_Recalc
	INTO #tmpCMS_duration
	FROM #tmpCMS_ID

	SELECT TOP 100 Duration_Unit
	              , Medication_Duration
				  , Duration_Recalc
	FROM #tmpCMS_duration


-- (4) Identify total of morphine mg equivalents (MME's) 
	       , CASE WHEN Medication IN ('BUPERNORPHINE', 'BUPRENORPHINE', 'BUPRENORPHINE TABLET', 'BUTORPHANOL', 'DIHYDROCODEINE',
                                      'TRAMADOL', 'buprenorphine', 'bupernorphine', 'butorphanol', 'dihydrocodeine', 'tramadol',
                                      'tramadol HCL', 'dihydrocodeine-acetaminophin-caff') 

	-- VA 
	SELECT DISTINCT Medication
	FROM PythonOER.dbo.VA_data
	
	DROP TABLE IF EXISTS #tmpVA_MME

	SELECT CASE WHEN Medication LIKE '%buprenorphine%' OR Medication LIKE '%bupernorphine%' THEN Dose_Recalc*30
             	WHEN Medication LIKE '%butorphanol%' THEN Dose_Recalc*7
				WHEN Medication LIKE '%dihydrocodeine%' THEN Dose_Recalc*0.25
				WHEN Medication LIKE '%tramadol%' THEN Dose_Recalc*0.1
				ELSE 0 END AS MME_VA
		   , *
	INTO #tmpVA_MME
	FROM #tmpVA_duration

	SELECT MME_VA, Medication, Dose_Recalc
	FROM #tmpVA_MME

	
	-- CMS
	SELECT DISTINCT Medication
	FROM PythonOER.dbo.CMS_Data

	DROP TABLE IF EXISTS #tmpCMS_MME

	SELECT CASE WHEN  Medication LIKE '%BUPRENORPHINE%' OR Medication LIKE '%BUPERNORPHINE%' THEN Dose_Recalc*30
		   WHEN Medication LIKE '%BUTORPHANOL%' THEN Dose_Recalc*7
		   WHEN Medication LIKE '%DIHYDRO%' THEN Dose_Recalc*0.25
		   WHEN Medication LIKE '%TRAMADOl%' THEN Dose_Recalc*0.1
		   ELSE 0 END AS MME_CMS
	       , *
	INTO #tmpCMS_MME
	FROM #tmpCMS_duration

	SELECT MME_CMS, Medication, Dose_Recalc
	FROM #tmpCMS_MME


-- (5) Merge together VA & CMS data frames
	-- This solution has been a bit lazy at subsetting our data frames. That is, I've relied a lot n the wildcard '*' without explicitly naming the columns to 
	-- retain all columns. In our merge, we will explicitly call the columns from both data frames. We can also alias columns with new names using the "... AS ###" 
	-- operator in our SELECT clauses


	DROP TABLE IF EXISTS #tmpMerge

	SELECT Patient_ID AS SSN_VA
	       , Visit_Date AS Visit_Date_VA
		   , Medication AS Medication_VA
		   , Age
		   , Height
		   , Weight
		   , Duration_Recalc AS Duration_Days_VA
		   , Dose_Recalc AS Dose_mg_VA
		   , Opioid AS Opioid_VA
		   , MME_VA
		   , b.* -- Selects all from our subquery below
	INTO #tmpMerge
	FROM #tmpVA_MME AS A
	FULL OUTER JOIN (SELECT Patient_ID_Edit AS SSN_CMS
					  , Visit_Date AS Visit_Date_CMS
					  , Medication AS Medication_CMS
					  , Duration_Recalc AS Duration_Days_CMS
					  , Dose_Recalc AS Dose_mg_CMS
					  , Opioid AS Opioid_CMS
					  , MME_CMS
				FROM #tmpCMS_MME) AS B
	ON A.Patient_ID = B.SSN_CMS

	SELECT TOP 10 * 
	FROM #tmpMerge

-- (6) Create and indicator variable to identify individuals dually enrolled in VA and CMS healthcare systems.
-- Here we can simply create the 
	DROP TABLE IF EXISTS #tmpDualEnrollment

	SELECT * 
	      , CASE WHEN SSN_VA IS NOT NULL AND SSN_CMS IS NOT NULL THEN 1
	       ELSE 0 END AS DualEnrollment
	INTO #tmpDualEnrollment
	FROM #tmpMerge
	
	SELECT DualEnrollment, COUNT(*) AS Freq
	FROM #tmpDualEnrollment
	GROUP BY DualEnrollment

	-- If we didn't want to store the results, we could also simply "create" the variable in a GROUP BY clause and count the grouped data: 
	SELECT CASE WHEN SSN_VA IS NOT NULL AND SSN_CMS IS NOT NULL THEN 1
	       ELSE 0 END AS DualEnrollment
		   , COUNT(*) AS Freq
	FROM #tmpMerge
	GROUP BY CASE WHEN SSN_VA IS NOT NULL AND SSN_CMS IS NOT NULL THEN 1
	       ELSE 0 END 


-- (7) Create a sum variable for total mg-morphine-equivalents within dual-use patients
	-- In creating a sum variable of MME for dual use patients, we are able to simply sum the two MME varibales 
	SELECT MME_CMS
	       , MME_VA
		   , MME_CMS + MME_VA AS MME_Total
	FROM #tmpDualEnrollment
	WHERE DualEnrollment=1

	-- But notice what happens for patients who are not dual enrolled (and so are missing MME_CMS) if we use the same simple addition to generate a MME_Total 
	SELECT MME_CMS
	       , MME_VA
		   , MME_CMS + MME_VA AS MME_Total
	FROM #tmpDualEnrollment
	WHERE DualEnrollment=0

	-- SQL will create a NULL value whenever we perform an operation that includes a NULL value
	-- Think of if as 3+2=5 or 4+0=4 BUT 4+NULL=NULL
	-- This often has unintended consequences. We could fix this a few ways, first with a somewhat annoying CASE WHEN clause
	SELECT MME_CMS
	       , MME_VA
		   , MME_CMS + MME_VA AS MME_Add
		   , CASE WHEN MME_VA IS NOT NULL AND MME_CMS IS NOT NULL THEN MME_CMS+MME_VA
		     WHEN MME_VA IS NOT NULL THEN MME_VA
			 ELSE MME_CMS END AS MME_CaseWhen
	FROM #tmpDualEnrollment
	WHERE DualEnrollment=0


	-- A useful function for operations like this is the COALESCE() function. This function takes a serieis of values or variables, and 
	-- retains only the the first non-NULL value, see below:
		SELECT COALESCE(NULL, 1, 5, 6, 7)
		SELECT COALESCE(1, NULL, 3, 2009193, 1)
		SELECT COALESCE(NULL, NULL, NULL, 'foo', 'hello world', 'foo', 'bar')

	-- So we could simply create a new MME variable using this coalesce	funtion
	-- For comparative purposes, we will again retain the MME_Add and MME_CaseWhen variables, but in practice you would only use one of the MME variables to retain

	SELECT MME_CMS
	    , MME_VA
		, MME_CMS + MME_VA AS MME_Add
		, CASE WHEN MME_VA IS NOT NULL AND MME_CMS IS NOT NULL THEN MME_CMS+MME_VA
		    WHEN MME_VA IS NOT NULL THEN MME_VA
			ELSE MME_CMS END AS MME_CaseWhen
		, COALESCE(MME_VA, 0) + COALESCE(MME_CMS, 0) AS MME_Coalesce
	FROM #tmpDualEnrollment
	WHERE DualEnrollment=0





