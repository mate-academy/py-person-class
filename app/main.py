class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    for human in people:
        Person(human["name"], human["age"])

    for human in people:
        if human.get("wife"):
            husband = Person.people[human["name"]]
            wife = Person.people[human["wife"]]
            wife.husband = husband
            husband.wife = wife
    return [person for name, person in Person.people.items()]
