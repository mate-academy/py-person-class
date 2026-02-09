class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_instance = [Person(human["name"], human["age"]) for human in people]
    for person in people:
        instance = Person.people[person["name"]]
        if person.get("wife"):
            instance.wife = Person.people[person["wife"]]
        if person.get("husband"):
            instance.husband = Person.people[person["husband"]]
    return person_instance
