from functools import lru_cache
import logging
from typing import List, Optional
import os
from fastapi import Depends, FastAPI, Request, Cookie
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, Union
from pydantic import BaseModel
from model.name import Name

from repository.names import get_names_repository
from repository.names.namesDB import NamesRepository
from repository.mysqldb import get_db

logging.basicConfig(format="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S")
logging.basicConfig(level=logging.DEBUG)

app = FastAPI()
greeting_var = os.getenv('GREETING')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Name(BaseModel):
    name: str


@app.get("/")
def read_root():
    return {"Hello": f"This is the Greeting: {greeting_var} \n of root dir "}

@app.post("/greeting")
def greeting(name: Optional[Name] = None):
    print(name)
    if name:
        return {"greet": f"Hello {greeting_var} {name}"}
    else:
        return {"greet": f"Hello auto"}


@app.get("/greeting_db")
def get_greeting_db(db: NamesRepository = Depends(get_db),
 name_id: Optional[int] = 1) -> Name: 
    repository = get_names_repository(db)
    return repository.get_name(name_id)


if __name__ == "__main__":  # pragma: no cover
    import uvicorn  # type: ignore

    uvicorn.run(app, host="0.0.0.0", port=8080, debug=DEBUG)
