INSERT INTO users (username, role)
VALUES (%s, %s)
RETURNING user_id, username, role;