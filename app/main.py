class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    for person in people:
        Person(person["name"], person["age"])

    for person in people:
        obj = Person.people[person["name"]]
        if "wife" in person and person["wife"]:
            obj.wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"]:
            obj.husband = Person.people[person["husband"]]

    return list(Person.people.values())
