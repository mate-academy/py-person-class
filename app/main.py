class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = {}

    for person in people:
        name = person["name"]
        age = person["age"]
        instance = Person(name, age)
        person_instances[name] = instance

    for person in people:
        name = person["name"]
        if "wife" in person:
            wife_name = person["wife"]
            wife_instance = person_instances.get(wife_name)
            if wife_instance:
                person_instances[name].wife = wife_instance
                wife_instance.husband = person_instances[name]

    return list(person_instances.values())
