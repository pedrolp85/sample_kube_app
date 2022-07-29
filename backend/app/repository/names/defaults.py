from .names import NamesRepository
from .namesDB import NamesRepositoryDatabase
from repository.mysqldb import get_db

from typing import Optional


def get_names_repository(db) -> NamesRepository:
    return NamesRepositoryDatabase(db)
    
        
