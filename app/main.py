class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    for person in people:
        Person(person["name"], person["age"])

    for person in people:
        select_person = Person.people[person["name"]]
        if "wife" in person and person["wife"]:
            select_person.wife = Person.people[person["wife"]]
        elif "husband" in person and person["husband"]:
            select_person.husband = Person.people[person["husband"]]

    return list(Person.people.values())
