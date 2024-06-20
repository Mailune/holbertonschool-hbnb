from abc import ABC, abstractmethod

class IPersistenceManager(ABC):
    @abstractmethod
    def save(self, entity):
        """
        Save an entity to the storage system.
        """
        pass

    @abstractmethod
    def get(self, entity_id, entity_type):
        """
        Retrieve an entity by its ID and type from the storage system.
        """
        pass

    @abstractmethod
    def update(self, entity):
        """
        Update an existing entity in the storage system.
        """
        pass

    @abstractmethod
    def delete(self, entity_id, entity_type):
        """
        Delete an entity by its ID and type from the storage system.
        """
        pass

    @abstractmethod
    def get_all(self, entity_type):
        """
        Retrieve all entities of a specified type from the storage system.
        """
        pass
