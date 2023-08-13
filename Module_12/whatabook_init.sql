
#Tavia Payne 
#August 11th 2023
#CYBR 410 Data/database 
#WhatABook Program application 

CREATE TABLE store (
    store_id    INT           NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)  NOT NULL,
    PRIMARY KEY(store_id)
);
CREATE TABLE book (
    book_id    INT            NOT NULL    AUTO_INCREMENT,
    book_name  VARCHAR(200)   NOT NULL,
    details    VARCHAR(500)   NULL,
    author     VARCHAR(200)   NOT NULL,
    PRIMARY KEY(book_id)
);
CREATE TABLE user (
    user_id     INT           NOT NULL    AUTO_INCREMENT,
    first_name  VARCHAR(75)   NOT NULL,
    last_name   VARCHAR(75)   NOT NULL,
    PRIMARY KEY(user_id)
);
CREATE TABLE wishlist (
    wishlist_id INT           NOT NULL    AUTO_INCREMENT,
    user_id     INT           NOT NULL,
    book_id     INT           NOT NULL,
    PRIMARY KEY(wishlist_id),
    FOREIGN KEY(user_id)
        REFERENCES user(user_id),
    FOREIGN KEY(book_id)
        REFERENCES book(book_id)
);

INSERT INTO store(locale)
    VALUES('West Palm Beach Fl 33401');

INSERT INTO book(book_name, author, details, book_id) 
VALUES('Grace by me', 'Lilly Haze', 'A book about putting yourself first', '001'); 

INSERT INTO book(book_name, author, details, book_id) 
VALUES('Love You, Hate You ', 'Maggie Brown', 'A book about Lovers to enemies', '002'); 

INSERT INTO book(book_name, author, details, book_id) 
VALUES('The seven deadly sins', 'Josh Beck', 'An manga that tells the story of the seven deadly sins', '003'); 

INSERT INTO book(book_name, author, details, book_id) 
VALUES('Hello world', 'Lilac Jones', 'A book about a girl growing up in the small town and ready to leave it behind', '004'); 

INSERT INTO book(book_name, author, details, book_id) 
VALUES('Killing Me softly ', 'Lilly Haze', 'Sequel to Grace By Me', '005'); 

INSERT INTO book(book_name, author, details, book_id) 
VALUES('Spell on you', 'Crystal West', 'A children book about halloween chronicles', '006'); 

INSERT INTO book(book_name, author, details, book_id) 
VALUES('Shhhhh!', 'Brianna Mac', 'A book about a girl with an easting disorder', '007'); 

INSERT INTO book(book_name, author, details, book_id) 
VALUES('To the moon and back', 'Lilly Haze', 'A book about childhood friend who grew apart, reunited and fall in love', '008'); 

INSERT INTO book(book_name, author, details, book_id) 
VALUES('I shouldve cheated', 'Lilly Haze', 'A book about a girl catching her boyfriend cheating', '009'); 

-------

INSERT INTO user(first_name, last_name) 
    VALUES('Grace', 'May');

INSERT INTO user(first_name, last_name)
    VALUES('Slim', 'Green');

INSERT INTO user(first_name, last_name)
    VALUES('Jada', 'Beach');
-----------
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Jada'), 
        (SELECT book_id FROM book WHERE book_name = 'Hello world')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Slim'),
        (SELECT book_id FROM book WHERE book_name = 'Shhhhh!')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Grace'),
        (SELECT book_id FROM book WHERE book_name = 'To the moon and back')
    );
