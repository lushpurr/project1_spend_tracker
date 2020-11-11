DROP TABLE transactions;
DROP TABLE merchants;
DROP TABLE tags;

CREATE TABLE tags (
    id SERIAL PRIMARY KEY, 
    category VARCHAR(255),
    active BOOLEAN
);

CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255), 
    active BOOLEAN
);
CREATE TABLE transactions (
    id SERIAL PRIMARY KEY, 
    amount FLOAT,
    merchant_id INT REFERENCES merchants(id) ON DELETE CASCADE,
    tag_id INT REFERENCES tags(id)
);
