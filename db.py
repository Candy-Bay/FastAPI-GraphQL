from orator import DatabaseManager, Schema, Model
import os
from dotenv import load_dotenv

load_dotenv()

DATABASES = {
    "mysql": {
        "driver": "mysql",
        "host": "localhost",
        "database": "testdb",
        "user": os.getenv('MYSQL_USERNAME'),
        "password": os.getenv('MYSQL_PASSWORD'),
        "prefix": "",
        "port": 3306
    }
}

db = DatabaseManager(DATABASES)
schema = Schema(db)
Model.set_connection_resolver(db)