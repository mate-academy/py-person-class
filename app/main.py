class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_instances = {}

    for person_info in people:
        name = person_info["name"]
        age = person_info["age"]
        person_instance = Person(name, age)
        person_instances[name] = person_instance

    for person_info in people:
        person_instance = person_instances[person_info["name"]]

        if "wife" in person_info:
            wife_name = person_info["wife"]
            if wife_name is not None:
                person_instance.wife = person_instances[wife_name]

        if "husband" in person_info:
            husband_name = person_info["husband"]
            if husband_name is not None:
                person_instance.husband = person_instances[husband_name]

    return list(person_instances.values())
