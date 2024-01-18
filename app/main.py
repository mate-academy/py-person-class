class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    instances = []
    for person in people:
        name = person["name"]
        age = person["age"]
        person_list = Person(name, age)
        instances.append(person_list)

    for person in people:
        if person.get("wife"):
            Person.people[person["name"]].wife = Person.people[person["wife"]]
        if person.get("husband"):
            Person.people[person["name"]].husband = (
                Person.people[person["husband"]]
            )

    return instances
