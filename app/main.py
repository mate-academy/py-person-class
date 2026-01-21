class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = []
    for person_dict in people:
        person = Person(person_dict["name"], person_dict["age"])
        person_instances.append(person)
    for person_dict, person_instance in zip(people, person_instances):
        if "wife" in person_dict and person_dict["wife"] is not None:
            wife_name = person_dict["wife"]
            if wife_name in Person.people:
                person_instance.wife = Person.people[wife_name]
            else:
                person_instance.wife = None
        if "husband" in person_dict and person_dict["husband"] is not None:
            husband_name = person_dict["husband"]
            if husband_name in Person.people:
                person_instance.husband = Person.people[husband_name]
            else:
                person_instance.husband = None
    return person_instances
