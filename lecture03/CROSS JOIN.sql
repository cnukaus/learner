SELECT COUNT(1)
FROM
(select *
from 
Flight_data f1 limit 100)
tab1
CROSS JOIN
(select *
from 
Flight_data f1 limit 10)
tab2

