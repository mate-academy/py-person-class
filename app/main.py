class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    persons = [Person(human["name"], human["age"]) for human in people]

    for human in people:
        current_person = Person.people[human["name"]]
        if human.get("wife"):
            current_person.wife = Person.people[human["wife"]]
        if human.get("husband"):
            current_person.husband = Person.people[human["husband"]]

    return persons
