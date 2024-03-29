In social network like Facebook or Twitter, people send friend requests and accept others’ requests as well. Now given two tables as below:

Table: friend_request
| sender_id | send_to_id |request_date|
|-----------|------------|------------|
| 1         | 2          | 2016-06-01 |
| 1         | 3          | 2016-06-01 |
| 1         | 4          | 2016-06-01 |
| 2         | 3          | 2016-06-02 |
| 3         | 4          | 2016-06-09 |

Table: request_accepted
| requester_id | accepter_id |accept_date |
|--------------|-------------|------------|
| 1            | 2           | 2016-06-03 |
| 1            | 3           | 2016-06-08 |
| 2            | 3           | 2016-06-08 |
| 3            | 4           | 2016-06-09 |
| 3            | 4           | 2016-06-10 |

Write a query to find the overall acceptance rate of requests rounded to 2 decimals, which is the number of acceptance divide the number of requests.

For the sample data above, your query should return the following result.

|accept_rate|
|-----------|
|       0.80|

-- Write your MySQL query statement below
SELECT ROUND(IFNULL((SELECT COUNT(*) FROM request_accepted) / (SELECT COUNT(*) FROM friend_request), 0), 2) AS 'accept_rate';
