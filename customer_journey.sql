SELECT * FROM customer_journey;

-- Common table expression to identify duplicate and remove duplicate rows and format other columns
WITH CleanRecords AS (
	SELECT 
		JourneyID,
		CustomerID,
		ProductID,
		VisitDate,
		UPPER(Stage) AS Stage,  -- Converts Stage values to uppercase for consistency in data analysis
		Action,
		COALESCE(Duration, ROUND(AVG(Duration) OVER (PARTITION BY VisitDate),2)) AS Duration,  -- Calculates the average duration for each date, using only numeric values
		ROW_NUMBER() OVER(PARTITION BY CustomerID, ProductID, VisitDate, Stage, Action
							ORDER BY JourneyID) AS RowNum -- Assigns a row number to each row within the partition to identify duplicates 
	FROM 
		customer_journey
	)
SELECT * 
FROM CleanRecords
WHERE RowNum = 1  -- Keeps only the first occurrence of each duplicate group identified in the CTE
ORDER BY JourneyID
;