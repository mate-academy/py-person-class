class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = []
    name_to_person = {
        person["name"]: Person(person["name"], person.get("age", 0))
        for person in people
    }

    for persons in people:
        person_instance = name_to_person[persons["name"]]

        if persons.get("wife") and persons["wife"] in name_to_person:
            person_instance.wife = name_to_person[persons["wife"]]

        if persons.get("husband") and persons["husband"] in name_to_person:
            person_instance.husband = name_to_person[persons["husband"]]

        person_instances.append(person_instance)

    return person_instances
