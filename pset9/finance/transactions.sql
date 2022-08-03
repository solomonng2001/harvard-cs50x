CREATE TABLE transactions (id INTEGER, symbol TEXT NOT NULL, name TEXT NOT NULL, shares INTEGER NOT NULL, price NUMERIC NOT NULL, datetime_str TEXT NOT NULL, user_id INTEGER NOT NULL, PRIMARY KEY(id), FOREIGN KEY(user_id) REFERENCES users(id));