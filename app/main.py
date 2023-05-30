class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    for human in people:
        Person(human["name"], human["age"])

    for human in people:
        person = Person.people[human["name"]]
        if human.get("wife"):
            person.wife = Person.people[human["wife"]]
        elif human.get("husband"):
            person.husband = Person.people[human["husband"]]
    return [instance for instance in Person.people.values()]
