class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for person in people:
        if person["name"] not in Person.people:
            Person(person["name"], person["age"])

    for person in people:
        person_instance = Person.people[person["name"]]

        if "wife" in person and person["wife"] is not None:
            if person["wife"] in Person.people:
                person_instance.wife = Person.people[person["wife"]]

        if "husband" in person and person["husband"] is not None:
            if person["husband"] in Person.people:
                person_instance.husband = Person.people[person["husband"]]

    return list(Person.people.values())
