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
);
CREATE TABLE transactions (
    id SERIAL PRIMARY KEY, 
    amount FLOAT,
    merchant_id INT REFERENCES merchants(id) ON DELETE CASCADE,
    tag_id INT REFERENCES tags(id) ON DELETE CASCADE 
);
