-- SQL & Excel Data Analytics Assignment
-- SQL dialect: MySQL 8.0

CREATE DATABASE IF NOT EXISTS analytics_assignment;
USE analytics_assignment;

DROP TABLE IF EXISTS Sales;
DROP TABLE IF EXISTS Employees;

CREATE TABLE Employees (
    Employee_ID INT PRIMARY KEY,
    Employee_Name VARCHAR(50),
    Department VARCHAR(30),
    Salary DECIMAL(10,2),
    City VARCHAR(30)
);

INSERT INTO Employees VALUES
(101,'Aarav Sharma','IT',55000,'Delhi'),
(102,'Diya Gupta','HR',42000,'Meerut'),
(103,'Rohan Verma','IT',68000,'Noida'),
(104,'Ananya Singh','Sales',48000,'Delhi'),
(105,'Kabir Jain','Sales',62000,'Ghaziabad'),
(106,'Meera Kapoor','Finance',72000,'Noida'),
(107,'Arjun Mehta','IT',59000,'Meerut'),
(108,'Isha Malhotra','Finance',65000,'Delhi'),
(109,'Vivaan Bansal','Sales',53000,'Noida'),
(110,'Sara Khan','HR',45000,'Meerut');

CREATE TABLE Sales (
    Order_ID INT PRIMARY KEY,
    Order_Date DATE,
    Employee_ID INT,
    Product VARCHAR(30),
    Units_Sold INT,
    Unit_Price DECIMAL(10,2),
    Payment_Method VARCHAR(20),
    Total_Sales DECIMAL(12,2),
    Discount DECIMAL(12,2),
    Profit DECIMAL(12,2),
    FOREIGN KEY (Employee_ID) REFERENCES Employees(Employee_ID)
);

INSERT INTO Sales VALUES
(1001,'2026-08-01',101,'Laptop',1,65000,'Online',65000,5000,60000),
(1002,'2026-08-02',104,'Mouse',5,800,'Card',4000,200,3800),
(1003,'2026-08-03',105,'Keyboard',3,1500,'UPI',4500,300,4200),
(1004,'2026-08-04',103,'Monitor',2,12000,'Online',24000,1500,22500),
(1005,'2026-08-05',109,'Laptop',2,65000,'Card',130000,10000,120000),
(1006,'2026-08-06',101,'Keyboard',4,1500,'UPI',6000,300,5700),
(1007,'2026-08-07',104,'Monitor',1,12000,'Online',12000,500,11500),
(1008,'2026-08-08',105,'Mouse',10,800,'UPI',8000,400,7600),
(1009,'2026-08-09',103,'Laptop',1,65000,'Card',65000,5000,60000),
(1010,'2026-08-10',109,'Monitor',3,12000,'Online',36000,2000,34000),
(1011,'2026-08-11',107,'Keyboard',6,1500,'UPI',9000,450,8550),
(1012,'2026-08-12',108,'Mouse',8,800,'Card',6400,300,6100);

-- TASK 1: SELECT
SELECT * FROM Employees;
SELECT Employee_ID, Employee_Name, Department FROM Employees;
SELECT Employee_Name AS Name, Salary AS Monthly_Salary FROM Employees;

-- TASK 2: WHERE, ORDER BY, AGGREGATES
SELECT * FROM Employees WHERE Salary > 60000;
SELECT * FROM Employees WHERE Department = 'IT';
SELECT * FROM Employees WHERE Salary BETWEEN 50000 AND 70000;
SELECT * FROM Employees ORDER BY Salary DESC;
SELECT COUNT(*) AS Employee_Count,
       SUM(Salary) AS Total_Salary,
       AVG(Salary) AS Average_Salary,
       MIN(Salary) AS Minimum_Salary,
       MAX(Salary) AS Maximum_Salary
FROM Employees;

-- TASK 3: GROUP BY & HAVING
SELECT Department, COUNT(*) AS Employee_Count,
       SUM(Salary) AS Total_Salary,
       AVG(Salary) AS Average_Salary
FROM Employees
GROUP BY Department;

SELECT Department, COUNT(*) AS Employee_Count,
       AVG(Salary) AS Average_Salary
FROM Employees
GROUP BY Department
HAVING AVG(Salary) > 55000;

-- TASK 4: JOINS
SELECT e.Employee_Name, e.Department, s.Order_ID, s.Product, s.Total_Sales
FROM Employees e
INNER JOIN Sales s ON e.Employee_ID = s.Employee_ID;

SELECT e.Employee_Name, e.Department, s.Order_ID, s.Product, s.Total_Sales
FROM Employees e
LEFT JOIN Sales s ON e.Employee_ID = s.Employee_ID;

SELECT e.Employee_Name, e.Department, s.Order_ID, s.Product, s.Total_Sales
FROM Employees e
RIGHT JOIN Sales s ON e.Employee_ID = s.Employee_ID;

-- TASK 5: SUBQUERIES
SELECT Employee_Name, Salary
FROM Employees
WHERE Salary > (SELECT AVG(Salary) FROM Employees);

SELECT Product, Unit_Price
FROM Sales
WHERE Unit_Price > (SELECT AVG(Unit_Price) FROM Sales);

-- END
