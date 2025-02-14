class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list:
    person_instances = []
    for person in people:
        name = person["name"]
        age = person["age"]
        person = Person(name, age)
        person_instances.append(person)

    for person in people:
        name = person["name"]
        person_instance = Person.people[name]

        if "wife" in person and person["wife"] is not None:
            spouse_name = person["wife"]
            person_instance.wife = Person.people[spouse_name]
        elif "husband" in person and person["husband"] is not None:
            spouse_name = person["husband"]
            person_instance.husband = Person.people[spouse_name]

    for person in person_instances:
        if person.wife is None:
            del person.wife
        if person.husband is None:
            del person.husband

    return person_instances
