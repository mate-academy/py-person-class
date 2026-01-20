class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}

    for person in people:
        name, age = person["name"], person["age"]
        Person(name, age)

    for person in people:
        name = person["name"]
        if "wife" in person and person["wife"]:
            Person.people[name].wife = Person.people[person["wife"]]
            Person.people[person["wife"]].husband = Person.people[name]

        if "husband" in person and person["husband"]:
            Person.people[name].husband = Person.people[person["husband"]]
            Person.people[person["husband"]].wife = Person.people[name]

    return list(Person.people.values())
