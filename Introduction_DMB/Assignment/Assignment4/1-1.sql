select dept_name, max(salary) as maximum_salary
from instructor
group by dept_name