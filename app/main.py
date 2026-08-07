class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    instances_list = [
        Person(person["name"], person["age"])
        for person in people
    ]
    for person in people:
        if person.get("husband", None):
            current_person = Person.people[person["name"]]
            current_person.husband = Person.people[person["husband"]]
        if person.get("wife", None):
            current_person = Person.people[person["name"]]
            current_person.wife = Person.people[person["wife"]]
    return instances_list
