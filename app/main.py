class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    @classmethod
    def add_wife(cls, person: dict) -> None:
        cls.people[person["name"]].wife = cls.people[person["wife"]]

    @classmethod
    def add_husband(cls, person: dict) -> None:
        cls.people[person["name"]].husband = cls.people[person["husband"]]


def create_person_list(people: list) -> list[Person]:

    for person in people:
        Person(person["name"], person["age"])

    for person in people:

        if "wife" in person and person["wife"] is not None:
            Person.add_wife(person)

        if "husband" in person and person["husband"] is not None:
            Person.add_husband(person)

    return [values for key, values in Person.people.items()]
