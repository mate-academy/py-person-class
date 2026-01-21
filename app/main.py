class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    # optional but recommended to avoid stale state in repeated calls/tests
    Person.people = {}

    # Build all Person instances (list comprehension, preserves order)
    person_list = [
        Person(person_dict["name"], person_dict["age"])
        for person_dict in people
    ]

    # Wire spouse references using dict.get
    for person_dict in people:
        person = Person.people[person_dict["name"]]

        wife_name = person_dict.get("wife")
        if wife_name is not None:
            person.wife = Person.people[wife_name]

        husband_name = person_dict.get("husband")
        if husband_name is not None:
            person.husband = Person.people[husband_name]

    return person_list
