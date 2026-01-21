class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}

    person_instances = []

    for person_dict in people:
        name = person_dict["name"]
        age = person_dict["age"]
        person_instance = Person(name, age)
        person_instances.append(person_instance)

    for person_dict in people:
        current_person_name = person_dict["name"]
        current_person_instance = Person.people[current_person_name]

        if "wife" in person_dict and person_dict["wife"] is not None:
            wife_name = person_dict["wife"]
            if wife_name in Person.people:
                current_person_instance.wife = Person.people[wife_name]

        if "husband" in person_dict and person_dict["husband"] is not None:
            husband_name = person_dict["husband"]
            if husband_name in Person.people:
                current_person_instance.husband = Person.people[husband_name]

    return person_instances
