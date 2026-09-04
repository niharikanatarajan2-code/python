CREATE TABLE IF NOT EXISTS Salesman(
    Salesman_id TEXT PRIMARY KEY,
    name TEXT,
    city TEXT,
    comission TEXT
);

INSERT INTO Salesman(Salesman_id, name, city, comission) VALUES
('5001', 'James Hoog', 'New York', '0.15'),
('5002', 'Niall Knite', 'Paris', '0.13'),
('5005', 'Pit Alex', 'Rome', '0.13'),
('5006', 'Mc Lyon', 'Paris', '0.14');

SELECT * FROM Salesman;

CREATE TABLE IF NOT EXISTS Customer(
    customer_id TEXT,
    cust_name TEXT PRIMARY KEY,
    city TEXT,
    grade TEXT,
    Salesman_id TEXT
);

INSERT INTO Customer(customer_id, cust_name, city, grade, Salesman_id) VALUES
("3002", "nick rimando", "new york", "100", "5001"),
("3007", "brad davis", "new york", "200", "5001"),
("3005", "grahm zusi", "california", "200", "5002"),
("3008", "julian green", "london", "300", "5002"),
("3004", "fabian johnson", "paris", "300", "5006");

CREATE TABLE IF NOT EXISTS Orders(
    ord_no TEXT PRIMARY KEY,
    purch_amt TEXT,
    ord_date TEXT,
    customer_id TEXT,
    Salesman_id TEXT
);

INSERT INTO Orders(ord_no, purch_amt, ord_date, customer_id, Salesman_id) VALUES
("70001", "150.5", "2012-10-05", "3005", "5002"),
("70009", "270.5", "2012-09-10", "3001", "5001"),
("70002", "65.26", "2012-10-05", "3002", "5003"),
("70004", "110.5", "2012-08-17", "3009", "5007"),
("70007", "948.5", "2012-09-10", "3005", "5005");

SELECT Customer.cust_name, Salesman.name, Salesman.city
FROM Customer
JOIN Salesman ON Customer.Salesman_id = Salesman.Salesman_id;

SELECT Orders.ord_no, Customer.cust_name, Customer.city AS cust_city, Salesman.name, Salesman.city AS sales_city
FROM Orders
JOIN Customer ON Orders.customer_id = Customer.customer_id
JOIN Salesman ON Orders.Salesman_id = Salesman.Salesman_id
WHERE Customer.city <> Salesman.city;

SELECT Orders.ord_no, Customer.cust_name, Customer.grade
FROM Orders
JOIN Customer ON Orders.customer_id = Customer.customer_id
JOIN Salesman ON Orders.Salesman_id = Salesman.Salesman_id
WHERE Customer.grade IS NOT NULL;

SELECT Customer.cust_name AS "Customer",
       Customer.city AS "city",
       Salesman.name AS "Salesman",
       Salesman.comission
FROM Customer
JOIN Salesman ON Customer.Salesman_id = Salesman.Salesman_id
WHERE CAST(Salesman.comission AS REAL) BETWEEN 0.12 AND 0.14;
