CREATE TABLE orders_fact (
  order_id SERIAL PRIMARY KEY,
  order_date DATE,
  total_amount DECIMAL(10, 2),
  author_key INT,
  publisher_key INT,
  customer_key INT
);

CREATE TABLE authors_dim (
  author_key SERIAL PRIMARY KEY,
  author_id INT,
  author_name VARCHAR(100),
  nationality VARCHAR(50)
);

CREATE TABLE books_dim (
  book_key SERIAL PRIMARY KEY,
  book_id INT,
  book_name VARCHAR(200),
  author_key INT,
  FOREIGN KEY (author_key) REFERENCES authors_dim(author_key)
);

CREATE TABLE order_items_fact (
  order_item_id SERIAL PRIMARY KEY,
  order_id INT,
  book_key INT,
  quantity INT,
  unit_price DECIMAL(10, 2),
  FOREIGN KEY (order_id) REFERENCES orders_fact(order_id),
  FOREIGN KEY (book_key) REFERENCES books_dim(book_key)
);

CREATE TABLE publishers_dim (
  publisher_key SERIAL PRIMARY KEY,
  publisher_id INT,
  publisher_name VARCHAR(100)
);
CREATE TABLE customers_dim (
  customer_key SERIAL PRIMARY KEY,
  customer_id INT,
  customer_name VARCHAR(100),
  phone VARCHAR(20)
);
CREATE TABLE book_publisher_bridge (
  book_key INT,
  publisher_key INT,
  PRIMARY KEY (book_key, publisher_key),
  FOREIGN KEY (book_key) REFERENCES books_dim(book_key),
  FOREIGN KEY (publisher_key) REFERENCES publishers_dim(publisher_key)
);