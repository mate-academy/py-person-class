class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person_data in people:
        person_instance = Person.people[person_data["name"]]
        if "wife" in person_data and person_data["wife"] is not None:
            person_instance.wife = Person.people[person_data["wife"]]
        if "husband" in person_data and person_data["husband"] is not None:
            person_instance.husband = Person.people[person_data["husband"]]

    return person_list
