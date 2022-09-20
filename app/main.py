class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []

    for person in people:
        result.append(Person(person["name"], person["age"]))

    for human in people:
        if human.get("wife") is not None:
            Person.people[human["name"]].wife \
                = Person.people[human["wife"]]
        elif human.get("husband") is not None:
            Person.people[human["name"]].husband \
                = Person.people[human["husband"]]

    return result
