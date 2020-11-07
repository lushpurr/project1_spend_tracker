DROP TABLE merchants;
DROP TABLE transactions;
DROP TABLE tags;

CREATE TABLE tags (
    id SERIAL PRIMARY KEY, 
    category INT,
)