SELECT * FROM customers;
SELECT * FROM geography;

-- Query to join cutomers table with geography table to get complete location details
SELECT 
	CustomerID,
	CustomerName,
	Email,
	Gender,
	Age,
	Country,
	City
FROM 
	customers AS C
LEFT JOIN 
	geography AS G
ON 
	C.GeographyID = G.GeographyID;
	