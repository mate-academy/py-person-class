class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:

        if not name:
            raise ValueError("Name cannot be empty")

        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:

    person_list = [
        Person(one_person["name"], one_person["age"])
        for one_person in people
    ]

    for one_person in people:
        current = Person.people[one_person["name"]]

        husband_name = one_person.get("husband")
        if husband_name is not None:
            current.husband = Person.people[husband_name]

        wife_name = one_person.get("wife")
        if wife_name is not None:
            current.wife = Person.people[wife_name]

    return person_list
