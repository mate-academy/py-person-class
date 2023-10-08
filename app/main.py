class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = [
        Person(person["name"], person["age"]) for person in people
    ]

    for ind in people:
        person_name = Person.people[ind["name"]]
        if ind.get("wife"):
            person_name.wife = Person.people[ind["wife"]]
        elif ind.get("husband"):
            person_name.husband = Person.people[ind["husband"]]

    return person_instances
