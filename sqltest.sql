--alter table employee update column address = "Blr" where id = 100;

update employee set address = "Blr" where id = 100;

--Write a query to retrieve the EmpFname and EmpLname in a single column as “FullName”.
--The first name and the last name must be separated with space.

select concat(EmpFname, " ", EmpLname) as full_name from employee;

--Write a query find number of  male employees whose DOB is between 02/05/1970 to 31/12/1975
SELECT COUNT(*)
FROM employee
WHERE gender = 'Male'
  AND dob BETWEEN TO_DATE('1970-05-02', 'YYYY-MM-DD') AND TO_DATE('1975-12-31', 'YYYY-MM-DD');


--Write a query to create a new table which consists of data and structure copied from the other table.
select * into employee from emp where 1=1;

--Write a query to get the current date.
select date.now(); --wrong
SELECT CURRENT_DATE() AS CurrentDate;
