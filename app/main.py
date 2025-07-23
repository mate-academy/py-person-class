class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    for sdf in people:
        Person(sdf["name"], sdf["age"])

    for data in people:
        person = Person.people[data["name"]]

        if "wife" in data and data["wife"]:
            person.wife = Person.people[data["wife"]]
        if "husband" in data and data["husband"]:
            person.husband = Person.people[data["husband"]]

    return list(Person.people.values())
