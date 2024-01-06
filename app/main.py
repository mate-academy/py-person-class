class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = [
        Person(person["name"], person["age"])
        for person in people
    ]

    for person in people:
        name = person["name"]
        if "wife" in person and person["wife"] is not None:
            name_wife = person["wife"]
            Person.people[name].wife = Person.people[name_wife]

        if "husband" in person and person["husband"] is not None:
            name_husband = person["husband"]
            Person.people[name].husband = Person.people[name_husband]

    return persons
