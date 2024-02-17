class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:

    person_instances = [
        Person(instance["name"], instance["age"]) for instance in people
    ]

    for person in people:
        if "wife" in person and person["wife"]:
            Person.people[person["name"]].wife = (
                Person.people.get(person["wife"])
            )
        if "husband" in person and person["husband"]:
            Person.people[person["name"]].husband = (
                Person.people.get(person["husband"])
            )

    return person_instances
