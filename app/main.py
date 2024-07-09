class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        person_obj = Person.people[person["name"]]
        if "wife" in person and person["wife"] is not None:
            person_obj.wife = Person.people[person["wife"]]
        elif "husband" in person and person["husband"] is not None:
            person_obj.husband = Person.people[person["husband"]]

    return result
