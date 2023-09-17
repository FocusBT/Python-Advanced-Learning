# from typing import Union
from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional
from enum import Enum
app = FastAPI()


@app.get('/')
def index():
    return 'hey'


@app.get('/blog/{id}')
def blog(id: float):
    return {'data': id}

# Query Parameter api
@app.get('/blog') # http://127.0.0.1:8000/blog/?limit=12&published=unpublished
def blogs(limit, published):
    return {limit, "are ", published}

@app.get("/items/{item_id}")   # http://0.0.0.0:8000/items/1?q=wasi
# if you add Optional keyword that means that is query parameter then you must give a default value
async def get_item(item_id: str, q: Optional[str], short: bool = False):
    item = {"item_id"}
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

@app.get("/items")
# the str | None shows that none is default value which means it is optional
# if there would be q: str = "True", this will be called required but optional
# the ... shows this query is required and it doesnt have any default value
async def read_items(q: str = Query(..., max_length=10, min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    
    return results

@app.get("/multiple_items")
# http://0.0.0.0:8000/multiple_items?q=foo&q=bar&q=okie&q=dokie
async def read_multiple_items(q: list[str] = Query(["foo", "bar"])):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    
    return results

@app.get("/hiddenquerry")
# the include_in_schema tell whether to show in the docs or not
async def hidden_querry_route(
    hidden_querry: str | None = Query(None, include_in_schema=False)
):
    if hidden_querry:
        return {"Hidden query found"}
    return {"Hidden query not found"}




# Post api
class Blog(BaseModel):
    title: str
    body: str
    # published: Optional(bool)


@app.post('/blog')
def postMethod(request: Blog ):
    return {'data': request}


