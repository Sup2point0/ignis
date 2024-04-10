DROP TABLE monsters;
DROP TABLE cards;

CREATE TABLE cards(
  id INT(10) PRIMARY KEY,
  name TEXT NOT NULL,
  art BYTES,
  type TEXT NOT NULL
);

CREATE TABLE monsters(
  id FOREIGN KEY REFERENCES 
  type TEXT NOT NULL,
  race TEXT NOT NULL,
  attribute ENUM('divine', 'light', 'dark', 'fire', 'water', 'earth', 'wind') NOT NULL,
);
