class calculator:
    """Calculator class"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        length = len(V1)

        ret = 0
        for i in range(length):
            ret += V1[i] * V2[i]
        print("Dot product is:", ret)
        return ret

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        length = len(V1)

        ret = []
        for i in range(length):
            ret.append(V1[i] + V2[i])
        print("Add Vector is :", ret)
        return ret

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        length = len(V1)

        ret = []
        for i in range(length):
            ret.append(V1[i] - V2[i])
        print("Sous Vector is:", ret)
        return ret
