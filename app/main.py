class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:

    list_of_objects = []
    for person in people:
        list_of_objects.append(Person(person["name"], person["age"]))

    for person in people:
        obj = Person.people[person["name"]]
        if "wife" in person and person["wife"] is not None:
            obj.wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"] is not None:
            obj.husband = Person.people[person["husband"]]
    return list_of_objects
