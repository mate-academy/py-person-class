class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_instances = [
        Person(name=person["name"],
               age=person["age"]
               )
        for person in people
    ]
    for person in people:
        if spouse := person.get("wife"):
            Person.people[spouse].husband = Person.people[person["name"]]
        elif spouse := person.get("husband"):
            Person.people[spouse].wife = Person.people[person["name"]]
    return person_instances
