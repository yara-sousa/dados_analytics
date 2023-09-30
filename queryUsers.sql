-- SQLite
CREATE TRIGGER alter_data
	BEFORE UPDATE ON table
	FOR EACH ROW
	SET NEW.dob = NOW();

UPDATE table 
SET last_name = "Sousa"
WHERE user_id >= 2;

SELECT * FROM users;
