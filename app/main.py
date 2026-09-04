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
                    self.__dict__[key] = value
        Person.people[name] = self

    def define_couple(self, key: str, name: str, other: str) -> None:
        self.__dict__[key] = self.get_person_by_name(name)
        if isinstance(self.__dict__[key], Person):
            self.__dict__[key].__dict__[other] = self

    def get_person_by_name(self, name: str) -> Person | str:
        for person_name_key in Person.people:
            if person_name_key == name:
                return Person.people[person_name_key]
        return name


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person_list.append(Person(**person))
    return person_list
