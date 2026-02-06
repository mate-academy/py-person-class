class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(entity["name"], entity["age"]) for entity in people]

    for entity in people:
        human = Person.people[entity["name"]]
        if entity.get("wife"):
            human.wife = Person.people[entity["wife"]]
        if entity.get("husband"):
            human.husband = Person.people[entity["husband"]]

    return person_list
