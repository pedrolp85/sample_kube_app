from typing import Optional

from model.name import Name
from .names import NamesRepository

from sqlalchemy.orm import Session

from repository.mysqldb import models




class NamesRepositoryDatabase(NamesRepository):
    def __init__(
        self, db: Session, skip: Optional[int] = 0, limit: Optional[int] = 100
    ) -> None:
        self._session = db


    def get_name(self, name_id: int) -> Name:
        name = (
            self._session.query(models.Name)
            .filter(models.Name.id == name_id)
            .first()
        )

        return name

