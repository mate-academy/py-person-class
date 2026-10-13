class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for person in people:
        Person(person["name"], person["age"])

    for person in people:
        name = Person.people[person["name"]]
        if person.get("wife") is not None:
            name.wife = Person.people[person["wife"]]
        elif person.get("husband") is not None:
            name.husband = Person.people[person["husband"]]

    return [value for value in Person.people.values()]
