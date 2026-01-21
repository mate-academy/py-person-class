class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_instances = []
    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person = Person(name, age)
        person_instances.append(person)

    for person_data in people:
        current_person = Person.people[person_data["name"]]
        if "wife" in person_data and person_data["wife"]:
            current_person.wife = Person.people[person_data["wife"]]
        if "husband" in person_data and person_data["husband"]:
            current_person.husband = Person.people[person_data["husband"]]

    return person_instances
