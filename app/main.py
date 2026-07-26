class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    # Fix 1: Use a list comprehension to instantiate Person objects
    person_list = [
        Person(person_dict["name"], person_dict["age"])
        for person_dict in people
    ]

    # Second pass: Link spouse relationships
    for person_dict in people:
        current_person = Person.people[person_dict["name"]]

        if person_dict.get("wife") is not None:
            current_person.wife = Person.people[person_dict["wife"]]

        if person_dict.get("husband") is not None:
            current_person.husband = Person.people[person_dict["husband"]]

    return person_list
