from datetime import datetime
import typing
from typing import List, Optional
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name = "Ivn Dorn"
    signup_ts: Optional[datetime] = None
    friends: List[int] = []

external_data = {
    'id': '123',
    'signup_ts': '2021-11-29 11:12',
    'friends': [1, 2, '3/1']
}
user = User(**external_data)

print(user.id)

print(repr(user.signup_ts))

print(user.friends)

print(user.dict())
