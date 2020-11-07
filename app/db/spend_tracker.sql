DROP TABLE tags;
DROP TABLE merchants;
DROP TABLE transactions;

CREATE TABLE tags (
    id SERIAL PRIMARY KEY, 
    category INT
);

CREATE TABLE transacations (
    id SERIAL PRIMARY KEY, 
    amount FLOAT
);

CREATE TABLE 