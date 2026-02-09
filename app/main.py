class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for human in people:
        person = Person(name=human["name"], age=human["age"])
        person_list.append(person)

    for human in people:
        person = Person.people[human["name"]]
        if "wife" in human and human["wife"] is not None:
            person.wife = Person.people[human["wife"]]
        if "husband" in human and human["husband"] is not None:
            person.husband = Person.people[human["husband"]]
    return person_list
