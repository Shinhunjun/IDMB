SELECT sec.course_id, sec.sec_id, COUNT(*) AS student_num
FROM takes AS t
RIGHT JOIN section AS sec ON t.course_id = sec.course_id AND t.sec_id = sec.sec_id
WHERE sec.year = 2017 AND sec.semester = 'Spring'
GROUP BY sec.course_id, sec.sec_id
HAVING COUNT(*) > 0;

