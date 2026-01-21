class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:

    Person.people.clear()

    for sdf in people:
        Person(sdf["name"], sdf["age"])

    for peoples in people:
        persons = Person.people[peoples["name"]]

        if "wife" in peoples and peoples["wife"]:
            persons.wife = Person.people[peoples["wife"]]
        if "husband" in peoples and peoples["husband"]:
            persons.husband = Person.people[peoples["husband"]]

    return list(Person.people.values())
