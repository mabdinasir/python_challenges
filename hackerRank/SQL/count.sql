-- COUNT
SELECT COUNT(NAME)
FROM CITY
WHERE POPULATION > 100000;


-- SUM
SELECT SUM(POPULATION)
FROM CITY
WHERE DISTRICT = 'California';

--AVG
SELECT AVG(POPULATION)
FROM CITY
WHERE DISTRICT = 'California';

--AVG with ROUND
SELECT ROUND(AVG(POPULATION), 0)
FROM CITY;

-- JAPAN Population
SELECT SUM(POPULATION)
FROM CITY
WHERE COUNTRYCODE = 'JPN';

-- Population Density Difference
SELECT MAX(POPULATION) - MIN(POPULATION)
FROM CITY;