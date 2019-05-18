### Q1
Tableau Reader can only access the local workbooks and Tableau View is working on Tableau Server.

### Q2
```sql
SELECT A.Country,A.la, B.latitude, A.lo, B.longitude
FROM
	(SELECT
	Country,
	AVG(Latitude) la,
	AVG(Longitude) lo
	FROM aviationdata
	GROUP BY 1) AS A
LEFT JOIN
	(SELECT *
	FROM countries) AS B
ON A.Country = B.`name`;
```

|                                                                |
|----------------------------------------------------------------|
| Country,la,latitude,lo,longitude                               |
| Brazil,-27.0575,-14.235004,-52.225278,-51.92528                |
| Bahamas,25.067223,25.03428,-77.492222,-77.39628                |
| Switzerland,47.457778,46.818188,8.548611,8.227512              |
| Chile,-33.806389,-35.675147,-70.465833,-71.542969              |
| "Dominican Republic",18.497222,18.735693,-68.958333,-70.162651 |
| Guyana,6.058889,4.860416,-58.779167,-58.93018                  |
| Italy,45.605278,41.87194,12.827223,12.56738                    |

### Q3
Countries_Cities = string.split(",")

### Q4
```sql
SELECT * FROM
(SELECT
Country,
`Airport.Name`,
Rank() over (PARTITION BY Country  ORDER BY length(`Airport.Name`) DESC) AS Ran
FROM aviationdata) AS A
WHERE A.Ran = 1;
```
