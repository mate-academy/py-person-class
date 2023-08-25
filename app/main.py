class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_instances = []

    for person_info in people:
        name = person_info["name"]
        age = person_info["age"]
        person_instance = Person(name, age)
        person_instances.append(person_instance)

    for person_info in people:
        person_instance = Person.people[person_info["name"]]

        if person_info.get("wife") is not None:
            person_instance.wife = Person.people[person_info.get("wife")]

        if person_info.get("husband") is not None:
            person_instance.husband = Person.people[person_info.get("husband")]

    return person_instances
