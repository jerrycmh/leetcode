select max(salary) as SecondHighestSalary from Employee where salary NOT IN(select MAX(salary) from Employee)