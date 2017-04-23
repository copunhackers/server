DROP TABLE USERS, MESSAGES CASCADE;

CREATE EXTENSION postgis;

CREATE TABLE MESSAGES (
    id               serial,
    content_type     text,
    content          text,
    username         text,
    creation_time    bigint,
    expiry_time      bigint,
    location         geography,
    PRIMARY KEY (id),
);
