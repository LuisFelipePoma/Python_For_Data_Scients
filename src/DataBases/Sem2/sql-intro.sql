CREATE TABLE Ages(
	name VARCHAR(128),
	age INTEGER
)

-- 
DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Krystyna', 19);
INSERT INTO Ages (name, age) VALUES ('Kashif', 14);
INSERT INTO Ages (name, age) VALUES ('Al', 32);
INSERT INTO Ages (name, age) VALUES ('Yangxi', 21);

-- 

SELECT hex(name || age) AS X FROM Ages ORDER BY X

-- Project 2

CREATE TABLE Counts (org Text, count INTEGER)