class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self
    pass


def create_person_list(people: list) -> list:
    person_instances = []

    for person_dict in people:
        name = person_dict["name"]
        age = person_dict["age"]
        person_instances.append(Person(name, age))

    for person_dict in people:
        name = person_dict["name"]
        person_instance = Person.people[name]

        if "wife" in person_dict and person_dict["wife"] is not None:
            wife_name = person_dict["wife"]
            person_instance.wife = Person.people[wife_name]

        if "husband" in person_dict and person_dict["husband"] is not None:
            husband_name = person_dict["husband"]
            person_instance.husband = Person.people[husband_name]

    return person_instances
    pass
