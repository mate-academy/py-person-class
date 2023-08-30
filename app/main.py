
class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[name] = self


def create_person_list(people_data: list) -> list:
    person_instances = []

    for person_dict in people_data:
        name = person_dict["name"]
        age = person_dict["age"]
        person_instance = Person(name, age)
        person_instances.append(person_instance)

    for person_instance, person_dict in zip(person_instances, people_data):
        if "wife" in person_dict and person_dict["wife"] in Person.people:
            person_instance.wife = Person.people[person_dict["wife"]]
        husband_name = person_dict.get("husband")
        if husband_name in Person.people:
            person_instance.husband = Person.people[husband_name]

        if person_dict.get("wife") is None:
            delattr(person_instance, "wife")

    return person_instances
