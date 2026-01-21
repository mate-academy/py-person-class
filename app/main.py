class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people_dicts: list[dict]) -> list[Person]:
    for person_data in people_dicts:
        name = person_data["name"]
        age = person_data["age"]
        Person(name, age)

    person_instances = []
    for person_data in people_dicts:
        current_person_name = person_data["name"]
        current_person_instance = Person.people[current_person_name]

        if "wife" in person_data and person_data["wife"] is not None:
            wife_name = person_data["wife"]
            wife_instance = Person.people[wife_name]
            current_person_instance.wife = wife_instance

        if "husband" in person_data and person_data["husband"] is not None:
            husband_name = person_data["husband"]
            husband_instance = Person.people[husband_name]
            current_person_instance.husband = husband_instance

        person_instances.append(current_person_instance)

    return person_instances
