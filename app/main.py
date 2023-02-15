class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self
    pass


def create_person_list(people: list) -> list:

    new_list = [Person(human["name"], human["age"]) for human in people]

    for person in people:
        if person.get("wife"):
            wife = Person.people[person.get("wife")]
            Person.people[person.get("name")].wife = wife
        if person.get("husband"):
            husband = Person.people[person.get("husband")]
            Person.people[person.get("name")].husband = husband
    return new_list
