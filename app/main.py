class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        self.people[self.name] = self


def create_person_list(people: list[dict]) -> list:
    for person in people:
        Person(person["name"], person["age"])

    for person in people:
        if "wife" in person and person["wife"] is not None:
            wife_ref = Person.people.get(person["wife"])
            Person.people[person["name"]].wife = wife_ref
        if "husband" in person and person["husband"] is not None:
            husband_ref = Person.people.get(person["husband"])
            Person.people[person["name"]].husband = husband_ref
    class_people = [person for person in Person.people.values()]
    return class_people
