class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = [
        Person(person["name"], person["age"])
        for person in people
    ]
    for human in people:
        if ("wife" in human) and (human["wife"] is not None):
            person = Person.people[human["name"]]
            person.wife = Person.people[human["wife"]]
        elif ("husband" in human) and (human["husband"] is not None):
            person = Person.people[human["name"]]
            person.husband = Person.people[human["husband"]]

    return result
