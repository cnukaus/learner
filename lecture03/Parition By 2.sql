WITH 
Ranked AS --THIS IS A TEMP RESULT SET
(SELECT 
row_number() OVER (PARTITION BY COUNTRY ORDER BY EVENT_DATE DESC) as rn
,Number_of_Engines
,lag(Number_of_Engines) over(order by country) as Prev_record
,lead(Number_of_Engines) over(PARTITION BY COUNTRY ORDER BY EVENT_DATE DESC) as next_record
/*,lag(Number_of_Engines,2) over(order by country) as Prev_2record 
,lead(Number_of_Engines) OVER (PARTITION BY COUNTRY ORDER BY EVENT_DATE DESC ) as next_record_same_partition */
,avg(Number_of_Engines) OVER (PARTITION BY COUNTRY ORDER BY EVENT_DATE DESC ROWS BETWEEN 1 PRECEDING AND 0 FOLLOWING) AS recent_Country_Engine_AVG
,sum(Number_of_Engines) OVER (PARTITION BY COUNTRY ORDER BY EVENT_DATE DESC ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING ) AS recent_Country_Engine_SUM 
,avg(Number_of_Engines) OVER (PARTITION BY COUNTRY ORDER BY EVENT_DATE DESC ROWS UNBOUNDED PRECEDING ) AS Country_Engine_AVG 
,sum(Number_of_Engines) OVER (PARTITION BY COUNTRY ORDER BY EVENT_DATE DESC ROWS UNBOUNDED PRECEDING ) AS Country_Engine_SUM 
,sum(Number_of_Engines) OVER () as total_engines
, COUNTRY
,EVENT_DATE
FROM 
Flight_data 
--WINDOW w AS (ORDER BY t)
)
SELECT * FROM Ranked;
SELECT

RN
,COUNTRY
,EVENT_DATE
FROM
Ranked 
WHERE rn<2
