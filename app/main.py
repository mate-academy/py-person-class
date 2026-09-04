class Person:
    people = {}

    def __init__(self, name: str, age: int, **kwargs) -> None:
        self.name = name
        self.age = age
        for key, value in kwargs.items():
            if value is not None:
                if (key == "husband"):
                    self.define_couple(key, value, "wife")
                elif (key == "wife"):
                    self.define_couple(key, value, "husband")
                else:
                    setattr(self, key, value)
        Person.people[name] = self

    def define_couple(self, key: str, name: str, other: str) -> None:
        setattr(self, key, self.get_person_by_name(name))
        if isinstance(self.__dict__[key], Person):
            setattr(self.__dict__[key], other, self)

    def get_person_by_name(self, name: str) -> Person | str:
        return Person.people.get(name, name)


def create_person_list(people: list) -> list:
    return [Person(**person) for person in people]
