-- Seed data for library database

-- Authors
INSERT INTO authors (name, bio) VALUES 
    ('Jorge Amado', 'Autor baiano famoso por obras como Capitaes da Areia'),
    ('Machado de Assis', 'Um dos maiores escritores brasileiros'),
    ('Clarice Lispector', 'Escritora українсько-бразилейра');

-- Books
INSERT INTO books (title, isbn, available_copies, author_id) VALUES
    ('Capitaes da Areia', '9788501000011', 5, 1),
    ('Dom Casmurro', '9788501000028', 3, 2),
    ('A Hora da Estrela', '9788501000035', 2, 3);

-- Members
INSERT INTO members (name, email, phone) VALUES
    ('Joao Silva', 'joao@email.com', '11999999999'),
    ('Maria Santos', 'maria@email.com', '11888888888'),
    ('Pedro Oliveira', 'pedro@email.com', '11777777777');

-- Loans
INSERT INTO loans (book_id, member_id, loan_date, return_date) VALUES
    (1, 1, CURRENT_TIMESTAMP, NULL),
    (2, 2, CURRENT_TIMESTAMP, NULL);