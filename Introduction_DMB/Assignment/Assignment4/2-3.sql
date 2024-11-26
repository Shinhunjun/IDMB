
INSERT INTO takes (ID, course_id, sec_id, semester, year)
SELECT s.ID, 'CS-001', '1', 'Spring', '2022'
FROM student AS s
WHERE s.dept_name = 'Comp. Sci.'
