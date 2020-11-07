DROP TABLE transactions;
DROP TABLE merchants;
DROP TABLE tags;

CREATE TABLE tags (
    id SERIAL PRIMARY KEY, 
    category INT
);

CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) 
)
CREATE TABLE transacations (
    id SERIAL PRIMARY KEY, 
    amount FLOAT,
    id INT REFERENCES merchants(id),
    id INT REFERENCES tag(id) 
);
