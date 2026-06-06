-- Data Cleaning


Select *
From scottish_cvd_df;


-- Create copy of data table

Create Table scottish_cvd_copy
Like scottish_cvd_df;

Select *
From scottish_cvd_copy;



Insert scottish_cvd_copy
Select *
From scottish_cvd_df;



-- Change sc and cvddef column names

Alter Table scottish_cvd_copy
Rename Column sc to `social class`,
Rename Column cvddef to `cvd status`;

Select * 
From scottish_cvd_copy;


-- Check for null values

Select *
From scottish_cvd_copy 
Where rownames IS NULL
	OR age IS NULL
    OR sex IS NULL
    OR `social class` IS NULL
    OR `cvd status` IS NULL
    OR carstair IS NULL
    OR smoke IS NULL
    OR area IS NULL;
    
Select * 
From scottish_cvd_copy;


-- Check and remove any duplicates 

Select rownames, id, count(*) as cnt
From scottish_cvd_copy
Group By rownames, id
Having count(*) > 1;


Select *
From scottish_cvd_copy
Order By rownames;


Delete From scottish_cvd_copy
Where id in (
		Select id 
		From (
				Select *
				, row_number() over (partition by rownames, id) as rn
				From scottish_cvd_copy) x
		Where x.rn > 1) ;
        
Select *
From scottish_cvd_copy
Where id = 15;


Select age, count(age) as age_count, smoke 
From scottish_cvd_copy
Where id < 1001
Group By age, smoke
Order By age;
