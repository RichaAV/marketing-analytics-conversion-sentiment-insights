SELECT * FROM engagement_data;

--Query to clean and normalise the enagagement_data table

SELECT 
	EngagementID,
	ContentID,
	CASE  --FormattingContentType column to ensure the text is more readable and standardized
		WHEN UPPER(ContentType) = 'SOCIALMEDIA' THEN 'SOCIAL MEDIA'
		ELSE UPPER(ContentType)
		END AS ContentType,
	SUBSTRING(ViewsClicksCombined, 1, CHARINDEX('-',ViewsClicksCombined) - 1) AS VIEWS, --Splitting ViewsClicksCombined column to individual columns
	SUBSTRING(ViewsClicksCombined, CHARINDEX('-',ViewsClicksCombined) + 1, LEN(ViewsClicksCombined)) AS CLICKS,
	EngagementDate
FROM
	engagement_data
WHERE 
	ContentType != UPPER('newsletter'); -- Filter our newspaper from ContentType column as it is not relevant in this case