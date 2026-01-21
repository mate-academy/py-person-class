class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances_list = []
    for person in people:
        person_new = Person(person["name"], person["age"])
        if "wife" in person and person["wife"] is not None:
            person_new.wife = person["wife"]
        if "husband" in person and person["husband"] is not None:
            person_new.husband = person["husband"]
        person_instances_list.append(person_new)
    for person in person_instances_list:
        if hasattr(person, "wife"):
            person.wife = Person.people[person.wife]
        if hasattr(person, "husband"):
            person.husband = Person.people[person.husband]
    return person_instances_list
