class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for person in people:
        Person(name=person["name"], age=person["age"])

    for person in people:
        if "wife" in person and person["wife"] is not None:
            wife_name = Person.people[person["wife"]]
            wife_name.husband = Person.people[person["name"]]

        if "husband" in person and person["husband"] is not None:
            husband_name = Person.people[person["husband"]]
            husband_name.wife = Person.people[person["name"]]

    return [person for person in Person.people.values()]
