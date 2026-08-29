SELECT 
    machine_id,
    ROUND(
        (
            SUM(timestamp) FILTER (WHERE activity_type = 'end') - 
            SUM(timestamp) FILTER (WHERE activity_type = 'start')
        )::NUMERIC / COUNT(DISTINCT process_id), 3
    ) AS processing_time
FROM Activity
GROUP BY machine_id;
