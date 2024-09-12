CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,
    login TEXT NOT NULL,
    password_hash BYTEA NOT NULL,
    salt BYTEA NOT NULL,
    display_name TEXT NOT NULL,
    user_role TEXT NOT NULL
);