SELECT i.ID, i.name, COUNT(DISTINCT t.course_id) AS courses_taught
FROM instructor AS i
JOIN teaches AS t ON i.ID = t.ID
GROUP BY i.ID, i.name
HAVING COUNT(DISTINCT t.course_id) >= 3;