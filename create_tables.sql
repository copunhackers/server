-- DROP Tables (For testing purposes)
DROP TABLE USERS, MESSAGES CASCADE;

CREATE EXTENSION postgis;

CREATE TABLE USERS (
    id              serial,
    name            text,
    PRIMARY KEY (id)
);

CREATE TABLE MESSAGES (
    id               serial,
    content_type     text,
    content          text,
    user_id          int,
    creation_time    bigint,
    expiry_time      bigint,
    location         geography(POINT,4326),
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES USERS(id)
);

--  INSERT INTO LIBRARIES VALUES
--  (0, 'Test Library', '127.0.0.1', 20, '55.947311, -3.201912');

--  INSERT INTO USERS VALUES
--  (DEFAULT, 'Basile', 'token'),
--  (DEFAULT, 'Jack', 'token'),
