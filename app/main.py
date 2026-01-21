class Person:

    people = {}

    def __init__(self, name: str, age: int, **kwargs) -> None:
        self.name = name
        self.age = age
        for key, value in kwargs.items():
            if value is not None:
                setattr(self, key, value)
        self.people[self.name] = self

    @classmethod
    def reset_people(cls) -> None:
        cls.people = {}


def create_person_list(people: list) -> list:
    Person.reset_people()
    for person in people:
        Person(**person)
    for person in people:
        if "wife" in person.keys() and person["wife"] is not None:
            Person.people[person["name"]].wife = Person.people[person["wife"]]
        if "husband" in person.keys() and person["husband"] is not None:
            Person.people[person["name"]].husband = (
                Person.people[person["husband"]])
    return list(Person.people.values())
