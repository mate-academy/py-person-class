class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = []
    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person = Person(name, age)
        person_instances.append(person)

    for person_data in people:
        name = person_data["name"]
        person_instance = Person.people[name]

        if "wife" in person_data and person_data["wife"] is not None:
            wife_name = person_data["wife"]
            person_instance.wife = Person.people[wife_name]
        elif "husband" in person_data and person_data["husband"] is not None:
            husband_name = person_data["husband"]
            person_instance.husband = Person.people[husband_name]

    return person_instances
