SELECT DISTINCT student.ID
FROM student
JOIN takes ON student.ID = takes.ID
JOIN teaches ON teaches.course_id = takes.course_id
JOIN instructor ON instructor.ID = teaches.ID
WHERE instructor.name = 'Katz';