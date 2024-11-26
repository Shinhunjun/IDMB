
SELECT DISTINCT c.course_id, c.title
FROM course AS c
JOIN section AS s 
ON c.course_id = s.course_id
JOIN time_slot AS t 
ON t.time_slot_id = s.time_slot_id
WHERE c.dept_name = 'Comp. Sci.'
  AND t.start_hr >= 12;