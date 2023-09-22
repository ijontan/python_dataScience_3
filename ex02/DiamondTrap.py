from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing the King family"""
    def __init__(self, first_name=None, is_alive=True):
        """contructor"""
        super().__init__(first_name, is_alive)

    def set_eyes(self, color):
        """set eyes color"""
        self.eyes = color

    def get_eyes(self):
        """get eyes color"""
        return self.eyes

    def set_hairs(self, color):
        """set hair color"""
        self.hair = color

    def get_hairs(self):
        """get hair color"""
        return self.hair
