from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family"""
    family_name: str
    eyes: str
    hair: str

    def __init__(self, first_name=None, is_alive=True):
        """Constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hair = "dark"

    def __str__(self):
        """String representation"""
        return f"('{self.family_name}', '{self.eyes}', '{self.hair}')"

    def __repr__(self):
        """String representation"""
        return f"Vector ('{self.family_name}', '{self.eyes}', '{self.hair}')"


class Lannister(Character):
    """Representing the Lannister family"""
    family_name: str
    eyes: str
    hair: str

    def __init__(self, first_name=None, is_alive=True):
        """Constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hair = "light"

    @staticmethod
    def create_lannister(first_name=None, is_alive=True):
        """Factory method"""
        return Lannister(first_name, is_alive)

    def __str__(self):
        """String representation"""
        return f"('{self.family_name}', '{self.eyes}', '{self.hair}')"

    def __repr__(self):
        """String representation"""
        return f"Vector ('{self.family_name}', '{self.eyes}', '{self.hair}')"
