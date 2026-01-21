class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    for human in people:
        result.append(Person(human["name"], human["age"]))

    for human in people:
        person = Person.people[human["name"]]
        if "wife" in human and human["wife"] is not None:
            person.wife = Person.people[human["wife"]]
            person.wife.husband = person

        if "husband" in human and human["husband"] is not None:
            person.husband = Person.people[human["husband"]]
            person.husband.wife = person
    return result
