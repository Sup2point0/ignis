-- create a new cards database

-- DROP TABLE monsters;
DROP TABLE cards;

CREATE TABLE cards(
  id INT(9) PRIMARY KEY,
  name TEXT NOT NULL,
  art BYTES,
  type TEXT NOT NULL
);

CREATE TABLE monsters(
  id INT(15) PRIMARY KEY,
  FOREIGN KEY(id) REFERENCES cards,
  type TEXT NOT NULL,
  race TEXT NOT NULL,
  attribute ENUM('divine', 'light', 'dark', 'fire', 'water', 'earth', 'wind') NOT NULL,
);
