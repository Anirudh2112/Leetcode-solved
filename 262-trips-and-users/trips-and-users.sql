# Write your MySQL query statement below
/* Trips and Users - LeetCode SQL Solution
 * 
 * This solution calculates the cancellation rate for each day between 
 * 2013-10-01 and 2013-10-03, where:
 * - Both client and driver must not be banned
 * - Cancellation rate = canceled trips / total trips (rounded to 2 decimal places)
 */

SELECT 
    t.request_at AS 'Day',
    ROUND(
        SUM(
            CASE 
                WHEN t.status = 'cancelled_by_driver' OR t.status = 'cancelled_by_client' THEN 1 
                ELSE 0 
            END
        ) / COUNT(*), 
        2
    ) AS 'Cancellation Rate'
FROM 
    Trips t
    JOIN Users c ON t.client_id = c.users_id AND c.banned = 'No'
    JOIN Users d ON t.driver_id = d.users_id AND d.banned = 'No'
WHERE 
    t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY 
    t.request_at;
