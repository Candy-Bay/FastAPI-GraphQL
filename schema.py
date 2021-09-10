import graphene

from serializers import (
    UserGrapheneInputModel,
    UserGrapheneModel
)
from db import db

from models.user import User

# Queries
class Query(graphene.ObjectType):
    # Define queries
    say_hello = graphene.String(name=graphene.String(default_value='Test Driven'))
    list_users = graphene.List(UserGrapheneModel)
    get_single_user = graphene.Field(UserGrapheneModel, user_id=graphene.NonNull(graphene.Int))
    get_single_user_by_address = graphene.Field(UserGrapheneModel, address=graphene.NonNull(graphene.String))
    # Define method for resolving querie
    # resolve_<query_definition_name>
    @staticmethod
    def resolve_say_hello(parent, info, name):
        return f'Hello {name}'


    @staticmethod
    def resolve_list_users(parent, info):
        return User.all()

    @staticmethod
    def resolve_get_single_user(parent, info, user_id):
        return User.find_or_fail(user_id)

    @staticmethod
    def resolve_get_single_user_by_address(parent, info, address):
        return db.table('users').where('address', address).first()


def updateUser():
    pass

# Mutations
class CreateUser(graphene.Mutation):
    class Arguments:
        user_details = UserGrapheneInputModel()

    Output = UserGrapheneModel

    @staticmethod
    def mutate(parent, info, user_details):
        db.table('users').where('address', user_details.address).delete()
        user = User()
        user.address = user_details.address
        user.discordID = user_details.discordID

        user.save()

        return user


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()