-- DATA ANALYSIS
-- 1
SELECT emp.emp_no, emp.last_name, emp.first_name, emp.gender, sal.salary
       FROM employees as emp
       LEFT JOIN salaries as sal
       ON (emp.emp_no = sal.emp_no)
;

-- 2
SELECT emp_no, first_name, last_name, hire_date
	   FROM employees
	   WHERE hire_date
	   BETWEEN '1986-01-01' AND '1986-12-31'
;

-- 3
SELECT man.dept_no, dep.dept_name, man.emp_no, emp.last_name,
       emp.first_name, man.from_date, man.to_date
	   FROM dept_manager AS man
       INNER JOIN departments AS dep
       ON (man.dept_no = dep.dept_no)
       INNER JOIN employees AS emp
       ON (man.emp_no = emp.emp_no)
;

-- 4
SELECT emp.emp_no, emp.last_name, emp.first_name, dep.dept_name
	   FROM employees AS emp
       INNER JOIN dept_emp AS de
       ON (emp.emp_no = de.emp_no)
       INNER JOIN departments AS dep
       ON (de.dept_no = dep.dept_no)
;

-- 5
SELECT emp_no, first_name, last_name
	   FROM employees
	   WHERE first_name = 'Hercules' AND last_name LIKE 'B%'
;

-- 6
SELECT emp.emp_no, emp.last_name, emp.first_name, dep.dept_name
	   FROM employees AS emp
       INNER JOIN dept_emp AS de
       ON (emp.emp_no = de.emp_no)
       INNER JOIN departments AS dep
       ON (de.dept_no = dep.dept_no)
	   WHERE dep.dept_name = 'Sales'
;

--7
SELECT emp.emp_no, emp.last_name, emp.first_name, dep.dept_name
       FROM employees AS emp
       INNER JOIN dept_emp AS de
       ON (emp.emp_no = de.emp_no)
       INNER JOIN departments AS dep
       ON (de.dept_no = dep.dept_no)
	   WHERE dep.dept_name IN ('Sales', 'Development')
;

--8
SELECT last_name, COUNT(last_name) AS empcount
	   FROM employees
	   GROUP BY last_name
	   ORDER BY empcount
	   DESC
;
