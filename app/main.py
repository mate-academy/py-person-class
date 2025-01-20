class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list) -> list:
    person_instances = []
    name_to_person = {}

    for person in people_data:
        name = person["name"]
        age = person["age"]
        person_instance = Person(name, age)
        name_to_person[name] = person_instance
        person_instances.append(person_instance)

    for person in people_data:
        name = person["name"]
        person_instance = name_to_person[name]

        if "wife" in person and person["wife"] is not None:
            person_instance.wife = name_to_person[person["wife"]]

        if "husband" in person and person["husband"] is not None:
            person_instance.husband = name_to_person[person["husband"]]

    return person_instances
