
from abc import ABC, abstractmethod

class Personaggio(ABC):

    def __init__(self, nome: str):
        self._nome = nome

    @abstractmethod
    def attacca(self):
        pass
    

class Guerriero(Personaggio):
    
    def attacca(self):
        return f"{self._nome} sferra un attacco con la spada"


class Mago(Personaggio):
    
    def attacca(self):
        return f"{self._nome} fa un incantesimo"

class Ladr(Personaggio):
    
    def attacca(self):
        return f"{self._nome} attacca con un pugnale"


if __name__ = "__main__":
  