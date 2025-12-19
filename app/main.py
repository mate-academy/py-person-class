class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    person_objects = [Person(p["name"], p["age"]) for p in people]

    for p in people:
        person_instance = Person.people[p["name"]]

        wife_name = p.get("wife")
        if wife_name is not None:
            person_instance.wife = Person.people[wife_name]

        husband_name = p.get("husband")
        if husband_name is not None:
            person_instance.husband = Person.people[husband_name]

    return person_objects
