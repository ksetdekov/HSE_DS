class Human:
    def __init__(self):
        pass


class Man(Human):
    def __init__(self):
        super().__init__()


class Woman(Human):
    def __init__(self):
        super().__init__()


def God():
    result = [Man(), Woman()]
    return result


paradise = God()

print(isinstance(paradise[0], Man))

print(type("d"))
