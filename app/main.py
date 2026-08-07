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

    [Person(person["name"], person["age"]) for person in people]

    for person in people:

        if person.get("wife") is not None:
            Person.add_wife(person)

        if person.get("husband") is not None:
            Person.add_husband(person)

    return [values for key, values in Person.people.items()]
