CREATE DATABASE desafiodev;

\c desafiodev;

-- Table Type Transactions
CREATE TABLE IF NOT EXISTS type_transaction (
    id_type int PRIMARY KEY,
    description varchar(255) NOT NULL,
    nature varchar(255) NOT NULL,
    signal varchar(1) NOT NULL
);

-- Insert types in type transaction
INSERT INTO type_transaction(id_type, description, nature, signal)
VALUES
    (1, 'Débito', 'Entrada', '+'),
    (2, 'Boleto', 'Saída', '-'),
    (3, 'Financiamento', 'Saída', '-'),
    (4, 'Crédito', 'Entrada', '+'),
    (5, 'Recebimento Empréstimo', 'Entrada', '+'),
    (6, 'Vendas', 'Entrada', '+'),
    (7, 'Recebimento TED', 'Entrada', '+'),
    (8, 'Recebimento DOC', 'Entrada', '+'),
    (9, 'Aluguel', 'Saída', '-');

-- Table Recipient
CREATE TABLE IF NOT EXISTS recipient (
    id serial PRIMARY KEY,
    cpf varchar(11) NOT NULL UNIQUE
);

-- Table Card
CREATE TABLE IF NOT EXISTS card (
    id serial PRIMARY KEY,
    card_number varchar(12) NOT NULL UNIQUE
);

-- Table Store
CREATE TABLE IF NOT EXISTS store (
    id serial PRIMARY KEY,
    balance decimal(20,2),
    store_name varchar(19) NOT NULL UNIQUE,
    store_owner varchar(14) NOT NULL
);

-- Table Transactions
CREATE TABLE IF NOT EXISTS transactions (
    id serial PRIMARY KEY,
    id_type int NOT NULL,
    date_occurrence date NOT NULL,
    value decimal(20,2) NOT NULL,
    recipient_id int NOT NULL,
    card_id int NOT NULL,
    hour_occurrence time with time zone NOT NULL,
    store_id int NOT NULL,
    FOREIGN KEY (id_type) REFERENCES type_transaction(id_type),
    FOREIGN KEY (recipient_id) REFERENCES recipient(id),
    FOREIGN KEY (card_id) REFERENCES card(id),
    FOREIGN KEY (store_id) REFERENCES store(id)
);