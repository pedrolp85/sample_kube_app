from typing import Optional

from pydantic import BaseModel

class Name(BaseModel):
    id: int
    name: Optional[str]
