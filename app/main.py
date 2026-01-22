class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    # First pass: Create all Person instances
    for person_dict in people:
        Person(person_dict["name"], person_dict["age"])

    # Second pass: Assign spouses
    for person_dict in people:
        person = Person.people[person_dict["name"]]
        wife = person_dict.get("wife")
        husband = person_dict.get("husband")

        if wife is not None:
            person.wife = Person.people.get(wife)
        if husband is not None:
            person.husband = Person.people.get(husband)

    return list(Person.people.values())
