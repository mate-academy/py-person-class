class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people_list: list) -> list:
    person_number = [
        Person(person["name"], person["age"])
        for person in people_list
    ]

    for person in people_list:
        person_data = Person.people[person["name"]]

        if "wife" in person and person["wife"] is not None:
            person_data.wife = Person.people[person["wife"]]
        elif "husband" in person and person["husband"] is not None:
            person_data.husband = Person.people[person["husband"]]

    return person_number
