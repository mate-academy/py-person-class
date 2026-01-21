class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    for person in people:
        Person(person["name"], person["age"])

    for person in people:
        human = Person.people[person["name"]]
        if "wife" in person and person["wife"]:
            human.wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"]:
            human.husband = Person.people[person["husband"]]

    return list(Person.people.values())
