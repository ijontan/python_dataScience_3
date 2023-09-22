from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class for characters"""
    first_name = None
    is_alive = True

    @abstractmethod
    def __init__(self):
        """Constructor"""
        pass

    def die(self):
        """Kill the character"""
        self.is_alive = False


class Stark(Character):
    """Stark class"""

    def __init__(self, first_name=None, is_alive=True):
        """Constructor"""
        self.first_name = first_name
        self.is_alive = is_alive
