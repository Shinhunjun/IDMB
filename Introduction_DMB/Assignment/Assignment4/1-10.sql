select distinct i.ID, i.name
from instructor as i
left join teaches as t
on i.ID = t.ID
left join takes as tk
on t.course_id = tk.course_id
where tk.ID not in (
select ID
from takes
where grade = 'A' or grade ='A-'
);
