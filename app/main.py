class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    persons = [Person(human["name"], human["age"]) for human in people]

    for i, human in enumerate(people):

        if human.get("wife"):
            persons[i].wife = Person.people.get(human["wife"])

        if human.get("husband"):
            persons[i].husband = Person.people.get(human["husband"])

    return persons
