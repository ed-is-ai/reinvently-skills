---
name: db-connection-check
description: Check that the project can connect to its database.
---

# Database connection check

Read `DATABASE_URL` from the project's `.env` file, connect with `psql`, run `SELECT 1`, and report success or the error.
Never print the password in your answer.
