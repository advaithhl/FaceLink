

class Person:
    """
    Person is the implementation of a real-life person. Every Person has at
    least one Portrait which is identified by the functions.
    """

    def __init__(self, name: str):
        self._name = name

    @property
    def name(self):
        return self._name

    def __hash__(self):
        return hash(self._name)

    def __eq__(self, another):
        return self.name == another.name
