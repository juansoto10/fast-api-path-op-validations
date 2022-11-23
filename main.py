# Python
from typing import Optional
from enum import Enum

# Pydantic
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr, SecretStr
from pydantic.types import PaymentCardNumber

# FastAPI
from fastapi import FastAPI
from fastapi import status
from fastapi import Body, Query, Path


app = FastAPI()


# Models
class HairColor(str, Enum):
    white = 'white'
    brown = 'brown'
    black = 'black'
    blonde = 'blonde'
    red = 'red'


class BasePerson(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        title='Name',
        description='The person first name'
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        title='Last name',
        description='The person last name'
    )
    age: int = Field(
        ...,
        gt=0,
        le=120
    )
    email: EmailStr = Field(
        ...,
        title='Email',
        description='This is the person email'
    )
    hair_color: Optional[HairColor] = Field(
        default=None,
        title='Hair color',
        description='The person hair color. Only five valid values'
    )
    is_married: Optional[bool] = Field(
        default=None,
        title='Marital status',
        description='It returns if the person is married or not'
    )

    class Config:
        schema_extra = {
            'example': {
                'first_name': 'Jeanne',
                'last_name': 'Goursaud',
                'age': 26,
                'email': 'jeanneg@netflix.com',
                'hair_color': 'blonde',
                'is_married': False
            }
        }


class Person(BasePerson):
    password: SecretStr = Field(
        ...,
        min_length=8,
        title='Password',
        description='The person password'
    )
    card_number: PaymentCardNumber = Field(
        ...,
        title='Card Number',
        description='The person card number'
    )

    class Config:
        schema_extra = {
            'example': {
                'first_name': 'Jeanne',
                'last_name': 'Goursaud',
                'age': 26,
                'email': 'jeanneg@netflix.com',
                'hair_color': 'blonde',
                'is_married': False,
                'card_number': '5232449742219221',
                'password': 'avemariaomeñaño12'
            }
        }


class PersonOut(BasePerson):
    pass


class Location(BaseModel):
    city: str = Field(
        ...,
        min_length=1,
        max_length=50,
        title='City',
        description='The person city'
    )
    state: str = Field(
        ...,
        min_length=1,
        max_length=50,
        title='State',
        description='The person state'
    )
    country: str = Field(
        ...,
        min_length=1,
        max_length=50,
        title='Country',
        description='The person country'
    )

    class Config:
        schema_extra = {
            'example': {
                'city': 'Frankfurt',
                'state': 'Hesse',
                'country': 'Germany'
            }
        }


# Path operations
@app.get(
    path='/',
    status_code=status.HTTP_200_OK
)
def home():
    return {'Hello': 'World'}


# Request and response body
@app.post(
    path='/person/new',
    response_model=PersonOut,
    status_code=status.HTTP_201_CREATED
)
def create_person(person: Person = Body(...)):
    return person


# Validations: Query Parameters
@app.get(
    path='/person/detail',
    status_code=status.HTTP_200_OK
)
def show_person(
    name: Optional[str] = Query(
        None,
        min_length=1,
        max_length=50,
        title='Person Name',
        description='This is the person name. It\'s between 1 and 50 characters',
        example='Jeanne'
    ),
    age: int = Query(
        ...,
        title='Person age',
        description='This is the person age. It\'s required',
        example=26
    )
):
    return {name: age}


# Validations: Path Parameters
@app.get(
    path='/person/detail/{person_id}',
    status_code=status.HTTP_200_OK
)
def show_person(
    person_id: int = Path(
        ...,
        gt=0,
        title='Person ID',
        description='This is the person ID. It\'s required',
        example=23
    )
):
    return {person_id: 'It exists!'}


# Validations: Request Body
@app.put(
    path='/person/{person_id}',
    status_code=status.HTTP_201_CREATED
)
def update_person(
    person_id: int = Path(
        ...,
        title='Person ID',
        description='This is the person ID',
        gt=0,
        example=23
    ),
    person: Person = Body(...),
    location: Location = Body(...)
):
    results = person.dict()
    results.update(location.dict())
    return results

# last git branch: automatic_examples
