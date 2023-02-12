class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for one_human in people:
        Person(one_human["name"], one_human["age"])

    for some_human in people:
        if "wife" in some_human and some_human["wife"] is not None:
            Person.people[some_human["name"]].wife \
                = Person.people[some_human["wife"]]
        if "husband" in some_human and some_human["husband"] is not None:
            Person.people[some_human["name"]].husband \
                = Person.people[some_human["husband"]]

    return list(Person.people.values())
