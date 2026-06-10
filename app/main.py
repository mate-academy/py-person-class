class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person in people:
        person_list.append(Person(person["name"], person["age"]))

    for person in people:
        person_obj = Person.people[person["name"]]
        if "wife" in person:
            if person["wife"] is not None:
                person_obj.wife = Person.people[person["wife"]]
        if "husband" in person:
            if person["husband"] is not None:
                person_obj.husband = Person.people[person["husband"]]

    return person_list
