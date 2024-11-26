SELECT i.ID, i.name
FROM instructor AS i
JOIN teaches AS t
ON i.ID = t.ID
JOIN course AS c
ON t.course_id = c.course_id
WHERE i.dept_name = c.dept_name
GROUP BY i.ID, i.name
HAVING COUNT(DISTINCT c.course_id) = (
    SELECT COUNT(*)
    FROM course AS c2
    WHERE c2.dept_name = i.dept_name
);