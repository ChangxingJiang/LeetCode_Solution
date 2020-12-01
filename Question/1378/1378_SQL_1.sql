Create table If Not Exists Employees
(
    id int,
    name varchar(20)
);
Create table If Not Exists EmployeeUNI
(
    id int,
    unique_id int
);

SELECT EmployeeUNI.unique_id,
       Employees.name
FROM Employees
         LEFT JOIN
    EmployeeUNI ON Employees.id = EmployeeUNI.id;