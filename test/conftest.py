import graphene
import pytest
from graphene.test import Client
from orator import DatabaseManager, Model, Schema
from orator.migrations import DatabaseMigrationRepository, Migrator

from models.user import User
from schema import Query, Mutation


@pytest.fixture(autouse=True)
def setup_database():
    DATABASES = {
        "sqlite": {
            "driver": "sqlite",
            "database": "test.db"
        }
    }

    db = DatabaseManager(DATABASES)
    Schema(db)

    Model.set_connection_resolver(db)

    repository = DatabaseMigrationRepository(db, "migrations")
    migrator = Migrator(repository, db)

    if not repository.repository_exists():
        repository.create_repository()

    migrator.reset("migrations")
    migrator.run("migrations")


@pytest.fixture(scope="module")
def client():
    client = Client(schema=graphene.Schema(query=Query, mutation=Mutation))
    return client


@pytest.fixture(scope="function")
def user():
    user = User()
    user.address = "0x3a96c519037e1a179C95634a96B3Ab0c7aE09a04"
    user.discordID = "875545081820622868"
    user.save()

    return user
