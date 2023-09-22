from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class for characters"""
    first_name: str
    is_alive: bool
    family_name: str
    eyes: str
    hair: str

    @abstractmethod
    def __init__(self, first_name=None, is_alive=True, family_name=None,
                 eyes=None, hair=None):
        """Constructor"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = family_name
        self.eyes = eyes
        self.hair = hair

    def die(self):
        """Kill the character"""
        self.is_alive = False


class Stark(Character):
    """Stark class"""

    def __init__(self, first_name=None, is_alive=True):
        """Constructor"""
        super().__init__(first_name, is_alive)
