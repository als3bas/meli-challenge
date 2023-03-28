CREATE TABLE customer (
  id SERIAL PRIMARY KEY,
  cust_name TEXT NOT NULL,
  fiscal_id TEXT NOT NULL,
  email TEXT NOT NULL,
  address TEXT NOT NULL
);

CREATE TABLE pos (
  id SERIAL PRIMARY KEY,
  serial TEXT NOT NULL,
  model TEXT NOT NULL,
  app_ver TEXT NOT NULL,
  cust_id INTEGER NOT NULL REFERENCES customer(id),
  active BOOLEAN NOT NULL
);

CREATE TABLE transactions (
  id SERIAL PRIMARY KEY,
  cust_id INTEGER NOT NULL REFERENCES customer(id),
  pmeth_id INTEGER NOT NULL,
  cod_aut TEXT NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  amount NUMERIC NOT NULL,
  status BOOLEAN NOT NULL,
  pos_id INTEGER NOT NULL REFERENCES pos(id)
);

---- add dummy data for all tables ---


