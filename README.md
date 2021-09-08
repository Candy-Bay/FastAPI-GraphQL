# FastAPI-GraphQL

Developed on Ubuntu 20.04

## Prerequisites

Python >= 3.8
MySQL >= 8.0.26

## Setup

In main directory:

`python3 -m venv venv`
`source venv/bin/activate`
`pip install -r requirement.txt`

Then create a .env file and add your MySQL login details. Like so:

```bash

MYSQL_USERNAME=<USERNAME>
MYSQL_PASSWORD=<PASSWORD>

```

To run the application execute:

`orator migrate -c db.py`

then...

`uvicorn main:app --reload`

Go to http://localhost:8000/graphql


## Resources

- https://testdriven.io/blog/fastapi-graphql/#orator-orm
- digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04