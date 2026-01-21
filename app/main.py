class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_with_person_inst = [
        Person(name=person["name"], age=person["age"])
        for person in people
    ]
    for human in people:
        person = Person.people[human["name"]]
        if "wife" in human and human["wife"] is not None:
            person.wife = Person.people[human["wife"]]
        elif "husband" in human and human["husband"] is not None:
            person.husband = Person.people[human["husband"]]

    return list_with_person_inst
