CREATE TABLE portfolio (id INTEGER, user_id INTEGER NOT NULL, symbol TEXT NOT NULL, name TEXT NOT NULL, shares INTEGER NOT NULL, current_price NUMERIC, FOREIGN KEY(user_id) REFERENCES users(id), PRIMARY KEY(id));