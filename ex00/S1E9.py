from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class for characters"""

    @abstractmethod
    def __init__(self):
        """Constructor"""
        pass


class Stark(Character):
    """Stark class"""
    first_name = None
    is_alive = True

    def __init__(self, first_name=None, is_alive=True):
        """Constructor"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Kill the character"""
        self.is_alive = False
