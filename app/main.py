class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    for human in people:
        Person.people[human["name"]] = Person(human["name"], human["age"])
        if human.get("husband"):
            wife = Person.people[human["name"]]
            husband = Person.people[human["husband"]]
            wife.husband = husband
            husband.wife = wife
    return [person for name, person in Person.people.items()]
