Create table If Not Exists Project
(
    project_id int,
    employee_id int
);
Create table If Not Exists Employee
(
    employee_id int,
    name varchar(10),
    experience_years int
);

SELECT project_id, ROUND(AVG(experience_years),2) AS average_years
FROM Project
         LEFT JOIN
     Employee E on Project.employee_id = E.employee_id
GROUP BY project_id;
