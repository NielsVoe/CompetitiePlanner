from abc import ABC, abstractmethod

class Serialize:
    @abstractmethod
    def ToDict(self) -> dict:
        """
        Convert the object to a dictionary representation.
        """
        pass

    @abstractmethod
    def FromDict(self, data: dict):
        """
        Populate the object from a dictionary representation.
        
        :param data: Dictionary containing the data to populate the object.
        """
        pass