# from typing import Union
from fastapi import FastAPI, Query, Path, Body, Cookie, Header
from pydantic import BaseModel, Field, HttpUrl, EmailStr
from typing import Optional
from enum import Enum
app = FastAPI()


@app.get('/')
def index():
    return 'hey'


# @app.get('/blog/{id}')
# def blog(id: float):
#     return {'data': id}

# # Query Parameter api
# @app.get('/blog') # http://127.0.0.1:8000/blog/?limit=12&published=unpublished
# def blogs(limit, published):
#     return {limit, "are ", published}

# @app.get("/items/{item_id}")   # http://0.0.0.0:8000/items/1?q=wasi
# # if you add Optional keyword that means that is query parameter then you must give a default value
# async def get_item(item_id: str, q: Optional[str], short: bool = False):
#     item = {"item_id"}
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}

# @app.get("/items")
# # the str | None shows that none is default value which means it is optional
# # if there would be q: str = "True", this will be called required but optional
# # the ... shows this query is required and it doesnt have any default value
# async def read_items(q: str = Query(..., max_length=10, min_length=3)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
    
#     return results

# @app.get("/multiple_items")
# # http://0.0.0.0:8000/multiple_items?q=foo&q=bar&q=okie&q=dokie
# async def read_multiple_items(q: list[str] = Query(["foo", "bar"])):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
    
#     return results

# @app.get("/hiddenquerry")
# # the include_in_schema tell whether to show in the docs or not
# async def hidden_querry_route(
#     hidden_querry: str | None = Query(None, include_in_schema=False)
# ):
#     if hidden_querry:
#         return {"Hidden query found"}
#     return {"Hidden query not found"}


# @app.get("/items_validation/{item_id}")
# # th * showes that when query parameter are passed it should be in order first  
# # q should be passed then item_id should be passed
# # other than Path is used to add integer validation
# async def read_items_validation(*, q : str = Query("defaultValue") ,item_id: int = Path(..., title="the ID to get", gt=10, le=100),):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q":q})
#     return results







# Part 7 -> Body - Mutiple Parameters



# # Post api
# class Blog(BaseModel):
#     title: str
#     body: str
#     published: bool

# class Item(BaseModel):
#     key: int

# @app.post('/blog')
# def postMethod(request: Blog, item: Item):
#     return {request, item}

# Part 8 -> Body - Field

# class Item(BaseModel):
#     name: str
#     des: str | None = Field(None, max_length=300)
#     price: float = Field(..., gt=0)
#     tax: float | None = None
# @app.put("/items/{item_id}")
# async def update_items(item_id: int, item: Item = Body(..., embed=True)):
#     results = {"item_id": item_id, "item": item}
#     return results


# Part 9 -> Body - Nested Modules

# class Image(BaseModel):
#     url: HttpUrl
#     name: str

# class Item(BaseModel):
#     name: str
#     tags: set[str] = []
#     image: Image | None = None
# class Offer(BaseModel):
#     offer_id: int = Field(..., gt=-1,lt=100)
#     items: list[Item]
# # now if you pass list of str but due to useage of set it will return only unique elements
# @app.post("/items")
# async def update_items(offer: Offer = Body(..., embed=True)):
#     return offer


# Part 10 -> Declare Request Example Data
# class Item(BaseModel):
#     name: str = Field(..., example="wase")
#     id: int = Field(..., example=12)
#     des: str = Field(..., max_length=300, example="desc")
# # in the each field you can give an example that will be shown in swagger docs
# # there is another way as wel in the function defination just add example and the whole json input
# # async def getItems(item_id: int, item: Item = Body(..., example={"name": "wasi", "id": 12, "des": "this is desc"})):
# @app.post("/items/{item_id}")
# async def getItems(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results
# # or there is one more method to do that we can use examples and make a dict,
# # examples={
#     # "normal": {
#     #     "name": "wasi",
#     #     "id": 12,
#     #     "des": "this is normal desc"
#     # },
#     # "extreme": {
#     #     "name": "wasay",
#     #     "id": 128,
#     #     "des": "this is extemere"
#     # }
# # }

# Part 12 -> Cookie and header
# @app.get("/items")
# async def read_items(
#     cookie_id: str | None = Cookie(None),
#     accept_encoding: str | None = Header(None),
#     user_agent: str | None = Header(None)
# ):
#     return {
#         "cookie_id": cookie_id,
#         "accept_encoding":accept_encoding,
#         "user_agent": user_agent
    # }


# Part 13 -> Response modal

class UserBase(BaseModel):
    user: str
    email: str
    full_name: str | None = None
# API will validate the response against the UserIn model and ensure that 
# it conforms to the specified structure and data types.
class UserIn(UserBase):
    password: str

class UserOut(UserBase):
    pass


# the UserOut defines what will be out output, and it is also shown in swagger docs
# you can see what will be input schema and what will be output schema
# or you can use response_modal_include or response modal_exclude to return the data you want
@app.post("/user/", response_model=UserOut, response_model_include={"name, email"})
async def create_user(user: UserIn):
    return user
