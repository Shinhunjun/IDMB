SELECT DISTINCT i.ID, i.name
FROM instructor AS i
LEFT JOIN teaches AS t ON i.ID = t.ID
LEFT JOIN takes AS tk ON t.course_id = tk.course_id AND t.sec_id = tk.sec_id
WHERE i.ID NOT IN (
    SELECT t.ID
    FROM teaches AS t
    JOIN takes AS tk ON t.course_id = tk.course_id AND t.sec_id = tk.sec_id
    WHERE tk.grade = 'A' OR tk.grade = 'A-'
);