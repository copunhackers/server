DROP TABLE MESSAGES;

CREATE EXTENSION postgis;

CREATE TABLE MESSAGES (
    id               serial,
    content_type     text,
    content          text,
    username         text,
    creation_time    bigint,
    expiry_time      bigint,
--    location         geography,
    lat              float,
    lng              float,
    PRIMARY KEY (id)
);
