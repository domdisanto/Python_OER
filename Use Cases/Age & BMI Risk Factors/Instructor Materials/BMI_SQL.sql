/*********************
Python OER
BMI Use Case
SQL "Solution"

Preface:
  Only working through the "original" data, not the provided updated data, essentially performing the first task in the student assessment in SQL but not the fourth
**********************/


-- Always useful to first examine your data
SELECT TOP 10 * 
FROM PythonOER.dbo.HeightWeight

SELECT TOP 10 * 
FROM PythonOER.dbo.ContactInfo


/*Running through the four criteria */

-- (1) BMI>=30
	-- Notice we use the variables from the table aliased as A (the height/weight table) to create the BMI variable 
	-- that we use in the WHERE... clause, but we only retain columns/fields from the contact information table (aliased as B)
	SELECT b.ID
		   , b.Address
		   , b.PhoneNo 
	FROM PythonOER.dbo.HeightWeight AS A -- Aliasing our data set 
	INNER JOIN PythonOER.dbo.ContactInfo AS B
	ON a.ID = B.ID 
	WHERE ROUND(a.[Weight (kg)] / POWER(a.[Height (cm)] / 100, 2), 2) >=30 -- Remember to round to the hundredths! 
			-- The POWER() function is used to  exponentiate our height variable 



-- (2) BMI>=35
	SELECT b.ID
		   , b.Address
		   , b.PhoneNo 
	FROM PythonOER.dbo.HeightWeight AS A -- Aliasing our data set 
	INNER JOIN PythonOER.dbo.ContactInfo AS B
	ON a.ID = B.ID 
	WHERE ROUND(a.[Weight (kg)] / POWER(a.[Height (cm)] / 100, 2), 2) >=35 -- Remember to round to the hundredths! 
			-- The POWER() function is used to  exponentiate our height variable 



-- (3) BMI>=30 & Age>=60
	-- Notice we use the variables from the table aliased as A (the height/weight table) to create the BMI variable 
	-- that we use in the WHERE... clause, but we only retain columns/fields from the contact information table (aliased as B)
	SELECT b.ID
		   , b.Address
		   , b.PhoneNo 
	FROM PythonOER.dbo.HeightWeight AS A -- Aliasing our data set 
	INNER JOIN PythonOER.dbo.ContactInfo AS B
	ON a.ID = B.ID 
	WHERE ROUND(a.[Weight (kg)] / POWER(a.[Height (cm)] / 100, 2), 2) >=30 -- Remember to round to the hundredths! 
			-- The POWER() function is used to  exponentiate our height variable 
		  AND a.Age>=60 -- Could also use b.Age, as the variable is present in both tables


-- (4) BMI>=35 & Age>=60
	SELECT b.ID
		   , b.Address
		   , b.PhoneNo 
	FROM PythonOER.dbo.HeightWeight AS A -- Aliasing our data set 
	INNER JOIN PythonOER.dbo.ContactInfo AS B
	ON a.ID = B.ID 
	WHERE ROUND(a.[Weight (kg)] / POWER(a.[Height (cm)] / 100, 2), 2) >=35 -- Remember to round to the hundredths! 
			-- The POWER() function is used to  exponentiate our height variable 
          AND a.Age>=60


