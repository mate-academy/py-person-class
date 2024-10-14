class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_people(people: list) -> list:
    person_instances = []
    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person = Person(name, age)
        person_instances.append(person)
    return person_instances


def set_spouses(people: list) -> None:
    for person_data in people:
        name = person_data["name"]
        person_instance = Person.people[name]
        spouse = person_data.get("wife") or person_data.get("husband")
        if spouse:
            if "wife" in person_data:
                person_instance.wife = Person.people[spouse]
            elif "husband" in person_data:
                person_instance.husband = Person.people[spouse]


def create_person_list(people: list) -> list:
    person_instances = create_people(people)
    set_spouses(people)
    return person_instances
