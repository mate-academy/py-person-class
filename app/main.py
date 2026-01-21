class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    for person in people:
        Person.people[person["name"]] = Person(person["name"], person["age"])

    for person in people:
        stored_person = Person.people[person["name"]]
        if "wife" in person and person["wife"]:
            stored_person.wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"]:
            stored_person.husband = Person.people[person["husband"]]

    return list(Person.people.values())
