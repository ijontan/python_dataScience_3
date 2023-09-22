class calculator:
    """Calculator class"""
    data: list

    def __init__(self, data) -> None:
        """Initialize"""
        self.data = data

    def __add__(self, object) -> None:
        """Add"""
        self.data = [x + object for x in self.data]
        print(self.data)

    def __mul__(self, object) -> None:
        """Multiply"""
        self.data = [x * object for x in self.data]
        print(self.data)

    def __sub__(self, object) -> None:
        """Subtract"""
        self.data = [x - object for x in self.data]
        print(self.data)

    def __truediv__(self, object) -> None:
        """Divide"""
        if object == 0:
            print("ERROR (div by zero)")
            return
        self.data = [x / object for x in self.data]
        print(self.data)
