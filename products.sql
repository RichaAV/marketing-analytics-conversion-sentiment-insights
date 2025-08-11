SELECT * FROM customer_journey;
SELECT * FROM customer_reviews;
SELECT * FROM products;
SELECT * FROM customers;

-- Query to categorise products based on their price
SELECT
	PRODUCTID, 
	PRODUCTNAME,
	PRICE,
	CASE 
		WHEN Price < 50 THEN 'Low'
		WHEN Price BETWEEN 50 AND 200 THEN 'Medium'
		ELSE 'High'
	END AS PriceCategory		
FROM products;