import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp
from fastapi.middleware.cors import CORSMiddleware
from schema import Query, Mutation

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_route('/graphql', GraphQLApp(schema=graphene.Schema(query=Query, mutation=Mutation)))

@app.get('/')
def ping():
    return {'ping': 'pong'}