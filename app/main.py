class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def not_none(person: dict, partner: str = "wife") -> bool:
    return person.get(partner) is not None


def create_person_list(people: list) -> list:
    people_instance = [
        Person(name=person["name"], age=person["age"])
        for person in people
    ]

    for index, person in enumerate(people):
        if not_none(person):
            people_instance[index].wife = Person.people[person["wife"]]

        if not_none(person, partner="husband"):
            people_instance[index].husband = Person.people[person["husband"]]
    return people_instance
