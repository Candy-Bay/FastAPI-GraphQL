from typing import List, Optional

from graphene_pydantic import PydanticInputObjectType, PydanticObjectType
from pydantic import BaseModel

class UserModel(BaseModel):
    id: int
    address: str
    discordID: str


class UserGrapheneModel(PydanticObjectType):
    class Meta:
        model = UserModel

class UserGrapheneInputModel(PydanticInputObjectType):
    class Meta:
        model = UserModel
        exclude_fields = ('id')
