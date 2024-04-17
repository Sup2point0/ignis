-- create a new cards database

DROP TABLE cards;

CREATE TABLE cards(
  id INT PRIMARY KEY,
  name TEXT NOT NULL,
  art BYTES NOT NULL,
  type TEXT,
  kind TEXT,
  race TEXT,
  attribute TEXT,
  level INT,
  attack INT,
  defense INT,
  pend INT
);
