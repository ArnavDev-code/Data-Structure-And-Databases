SELECT e.left_operand	, e.operator , e.right_operand,
CASE
    WHEN e.operator = '>' AND lo.value > ro.value THEN 'true'
    WHEN e.operator = '<' AND lo.value < ro.value THEN 'true'
    WHEN e.operator = '=' AND lo.value = ro.value THEN 'true'
    ELSE 'false'
    END AS value
FROM expressions e
JOIN variables lo ON e.left_operand = lo.name
JOIN variables ro ON e.right_operand = ro.name