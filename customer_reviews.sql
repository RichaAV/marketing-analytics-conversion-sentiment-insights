SELECT * FROM customer_reviews;

-- Query to clean whitespace issues in the ReviewText column
SELECT 
	ReviewID,
	CustomerID,
	ProductID,
	ReviewDate,
	Rating,
	REPLACE(ReviewText, '  ', ' ') AS ReviewText -- Cleans up the ReviewText by replacing double spaces with single spaces to ensure the text is more readable and standardized
FROM 
	customer_reviews;