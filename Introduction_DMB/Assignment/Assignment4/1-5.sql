select ID, name
from instructor 
where salary = (SELECT max(salary) FROM instructor)