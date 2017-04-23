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

GRANT ALL PRIVILEGES ON TABLE messages TO copunhackers;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO copunhackers;
