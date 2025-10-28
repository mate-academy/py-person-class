class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.spouse = None

        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_instances = []

    for person in people:
        instance = Person(person["name"], person["age"])
        person_instances.append(instance)

    for person in people:
        name = person["name"]
        instance = Person.people[name]

        relationship_key = None
        spouse_name = None

        if "wife" in person and person["wife"] is not None:
            relationship_key = "wife"
            spouse_name = person["wife"]

        elif "husband" in person and person["husband"] is not None:
            relationship_key = "husband"
            spouse_name = person["husband"]

        if spouse_name and spouse_name in Person.people:
            spouse_instance = Person.people[spouse_name]

            setattr(instance, relationship_key, spouse_instance)

    return person_instances
