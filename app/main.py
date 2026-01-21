class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    new_list = [Person(p["name"], p["age"]) for p in people]
    for person in people:
        persone_instance = Person.people[person["name"]]
        if "wife" in person and person["wife"]:
            persone_instance.wife = Person.people[person["wife"]]
        elif "husband" in person and person["husband"]:
            persone_instance.husband = Person.people[person["husband"]]
    return new_list
