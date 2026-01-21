class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = []

    for person in people:
        person_instance = Person(name=person["name"], age=person["age"])

        if "wife" in person and person["wife"] is not None:
            person_instance.wife = None
        if "husband" in person and person["husband"] is not None:
            person_instance.husband = None

        person_instances.append(person_instance)

    for person in people:
        current_person = Person.people[person["name"]]
        if "wife" in person and person["wife"]:
            current_person.wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"]:
            current_person.husband = Person.people[person["husband"]]

    return person_instances
