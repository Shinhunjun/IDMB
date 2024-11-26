SELECT s.ID, s.name 
FROM student AS s
WHERE s.dept_name = 'History'
AND NOT EXISTS (
    SELECT 1
    FROM takes AS t
    JOIN course AS c ON t.course_id = c.course_id
    WHERE s.ID = t.ID
    AND c.dept_name = 'Music'
);