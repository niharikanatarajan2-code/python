CREATE TABLE IF NOT EXISTS Restaurant(
    name TEXT,
    neighbourhood TEXT, 
    cuisine TEXT,
    review REAL,
    price TEXT,
    health TEXT
);
INSERT INTO Restaurant(name,neighbourhood,cuisine,review,price,health)
VALUES
('Peter','Brooklyn','Steak',4.4,'$$$$','A'),
('Jongro','Midtown','Korean',3.5,'$$','A'),
('Pocha','Midtown','Pizza',4.0,'$$$','B'),
('Lighthouse','Queens','Chinese',3.9,'$','A'),
('Minca','Downtown','American',4.6,'$$$',''),
('Marea','Chinatown','Chinese',3.0,'$$',''),
('Dirty Candy','Uptown','Italian',4.9,'$$$$','B'),
('Di Fara Pizza','Brooklyn','Pizza',3.8,'$$','A'),
('Golden Unicorn','Uptown','Italian',3.8,'$$','A');
SELECT DISTINCT neighbourhood
FROM Restaurant;
SELECT DISTINCT cuisine
FROM Restaurant;
SELECT*
FROM Restaurant
WHERE review>=4.0;
SELECT*
FROM Restaurant
WHERE cuisine='Italian'
AND price IN ('$$','$$$');