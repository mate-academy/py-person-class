class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = []
    for person_dict in people:
        person_instance = Person(person_dict["name"], person_dict["age"])
        person_instances.append(person_instance)

    for person_dict in people:
        person = Person.people[person_dict["name"]]
        if "wife" in person_dict and person_dict["wife"] is not None:
            wife_name = person_dict["wife"]
            wife = Person.people[wife_name]
            person.wife = wife
        if "husband" in person_dict and person_dict["husband"] is not None:
            husband_name = person_dict["husband"]
            husband = Person.people[husband_name]
            person.husband = husband

    return person_instances
