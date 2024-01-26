DROP TABLE IF EXISTS information;

CREATE TABLE information(
	ID INTEGER NOT NULL PRIMARY KEY,
	content VARCHAR(200) NOT NULL
);

INSERT INTO information (content) VALUES ("No order post");