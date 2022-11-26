# Python
from typing import Optional
from enum import Enum

# Pydantic
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr, SecretStr, PaymentCardNumber

# FastAPI
from fastapi import FastAPI
from fastapi import status
from fastapi import HTTPException
from fastapi import Body, Query, Path, Form, Header, Cookie, UploadFile, File


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


class LoginOut(BaseModel):
    username: str = Field(
        ...,
        max_length=20,
        example='katarinacodes'
    )
    message: str = Field(default='Login successful')


# Path operations
@app.get(
    path='/',
    status_code=status.HTTP_200_OK,
    tags=['Home']
)
def home():
    return {'Hello': 'World'}


# Request and response body
@app.post(
    path='/person/new',
    response_model=PersonOut,
    status_code=status.HTTP_201_CREATED,
    tags=['People']
)
def create_person(person: Person = Body(...)):
    return person


# Validations: Query Parameters
@app.get(
    path='/person/detail',
    status_code=status.HTTP_200_OK,
    tags=['People']
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

people = [1, 2, 3, 4, 5]


@app.get(
    path='/person/detail/{person_id}',
    status_code=status.HTTP_200_OK,
    tags=['People']
)
def show_person(
    person_id: int = Path(
        ...,
        gt=0,
        title='Person ID',
        description='This is the person ID. It\'s required',
        example=4
    )
):
    if person_id not in people:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='This person does not exist.'
        )
    return {person_id: 'It exists!'}


# Validations: Request Body
@app.put(
    path='/person/{person_id}',
    status_code=status.HTTP_201_CREATED,
    tags=['People']
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


@app.post(
    path='/login',
    response_model=LoginOut,
    status_code=status.HTTP_200_OK,
    tags=['People']
)
def login(username: str = Form(...), password: str = Form(...)):
    return LoginOut(username=username)


# Cookies and headers parameters

@app.post(
    path='/contact',
    status_code=status.HTTP_200_OK,
    tags=['Contact']
)
def contact(
    first_name: str = Form(
        ...,
        max_length=20,
        min_length=1
    ),
    last_name: str = Form(
        ...,
        max_length=20,
        min_length=1
    ),
    email: EmailStr = Form(...),
    message: str = Form(
        ...,
        min_length=20
    ),
    user_agent: Optional[str] = Header(default=None),
    ads: Optional[str] = Cookie(default=None)
):
    return user_agent


# Files

@app.post(
    path='/post-image',
    status_code=status.HTTP_201_CREATED,
    tags=['Upload']
)
def post_image(
    image: UploadFile = File(...)
):
    return {
        'Filename': image.filename,
        'Format': image.content_type,
        'Size(KB)': round(len(image.file.read())/1024, ndigits=2)
    }
