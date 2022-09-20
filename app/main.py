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
        if "husband" in person and person["husband"] in Person.people:
            human.husband = Person.people[person["husband"]]
        elif "wife" in person and person["wife"] in Person.people:
            human.wife = Person.people[person["wife"]]

    return list(Person.people.values())
