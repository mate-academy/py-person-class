class Person:
    people = {}

    def __init__(self, name: str, age: int) -> dict:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for one in people:
        Person(one["name"], one["age"])
    for person in people:
        if "wife" in person and person["wife"] is not None:
            Person.people[person["name"]].__dict__["wife"] \
                = Person.people[person["wife"]]
        if "husband" in person and person["husband"] is not None:
            Person.people[person["name"]].__dict__["husband"] \
                = Person.people[person["husband"]]
        person_list.append(Person.people[person["name"]])
    return person_list
