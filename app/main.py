class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list[Person]:
    for person in people:
        Person(person["name"], person["age"])
    for human in people:
        if "wife" in human and not human["wife"] is None:
            Person.people[human["name"]].wife \
                = Person.people[human["wife"]]
        if "husband" in human and not human["husband"] is None:
            Person.people[human["name"]].husband \
                = Person.people[human["husband"]]
    return list(Person.people.values())
