class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for human in people:
        Person(human["name"], human["age"])
    for human in people:
        if "wife" in human and human["wife"] is not None:
            wife = Person.people[human["wife"]]
            Person.people[human["name"]].wife = wife

        if "husband" in human and human["husband"] is not None:
            husband = Person.people[human["husband"]]
            Person.people[human["name"]].husband = husband

    return list(Person.people.values())
