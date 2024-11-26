SELECT c1.course_id AS prerequisite_id, c1.title AS prerequisite_title
FROM course AS c
JOIN prereq AS p 
ON p.course_id = c.course_id
JOIN course AS c1 
ON p.prereq_id = c1.course_id
WHERE c.title = 'Robotics';