from abc import ABC, abstractmethod

class OrderProcessor(ABC):

    @abstractmethod
    def process(self,order:dict) -> dict:
        pass