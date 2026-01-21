class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        obj = Person.people[person["name"]]
        if person.get("wife"):
            obj.wife = Person.people[person["wife"]]
        if person.get("husband"):
            obj.husband = Person.people[person["husband"]]
    return result
