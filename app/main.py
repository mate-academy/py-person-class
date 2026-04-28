class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    # First pass: create all Person instances
    person_objects = []

    for person_data in people:
        person = Person(person_data["name"], person_data["age"])
        person_objects.append(person)

    # Second pass: link relationships
    for person_data in people:
        current_person = Person.people[person_data["name"]]

        wife_name = person_data.get("wife")
        if wife_name is not None:
            current_person.wife = Person.people[wife_name]

        husband_name = person_data.get("husband")
        if husband_name is not None:
            current_person.husband = Person.people[husband_name]

    return person_objects
