SELECT s.ID, s.name, COUNT(t.grade) AS a_grade_count
FROM student AS s
JOIN takes AS t ON s.ID = t.ID
WHERE t.grade = 'A'
GROUP BY s.ID, s.name
HAVING COUNT(t.grade) = (
    SELECT MAX(a_grade_count)
    FROM (
        SELECT COUNT(grade) AS a_grade_count
        FROM takes
        WHERE grade = 'A'
        GROUP BY ID
    ) AS subquery
);