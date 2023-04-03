class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:

    person_list = [Person(entity["name"], entity["age"]) for entity in people]

    for entity in people:
        if entity.get("wife"):
            husband = Person.people[entity["name"]]
            husband.wife = Person.people[entity["wife"]]
        elif entity.get("husband"):
            wife = Person.people[entity["name"]]
            wife.husband = Person.people[entity["husband"]]

    return person_list
