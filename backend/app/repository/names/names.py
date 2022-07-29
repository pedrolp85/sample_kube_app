from abc import ABCMeta, abstractmethod
from typing import List, Optional



from model.name import Name 

class NamesRepository(metaclass=ABCMeta):
    
    @abstractmethod
    def get_name(self, id: int) -> Name:
        pass

