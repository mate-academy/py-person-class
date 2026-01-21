class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = []

    for person_dict in people:
        name = person_dict["name"]
        age = person_dict["age"]
        person_instance = Person(name, age)
        person_instances.append(person_instance)

    for person_dict in people:
        name = person_dict["name"]
        person_instance = Person.people[name]

        wife_name = person_dict.get("wife")
        if wife_name is not None:
            wife_instance = Person.people[wife_name]
            person_instance.wife = wife_instance

        husband_name = person_dict.get("husband")
        if husband_name is not None:
            husband_instance = Person.people[husband_name]
            person_instance.husband = husband_instance

    return person_instances
