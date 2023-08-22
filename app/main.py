class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = [Person(human["name"], human["age"]) for human in people]
    for human in people:
        person = Person.people[human["name"]]
        if human.get("wife", None):
            person.wife = Person.people[human["wife"]]
        elif human.get("husband", None):
            person.husband = Person.people[human["husband"]]
    return result
