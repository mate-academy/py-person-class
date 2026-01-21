class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    for person in people:
        Person(person["name"], person["age"])

    for person in people:
        per_instance = Person.people[person["name"]]
        if person.get("wife"):
            per_instance.wife = Person.people[person["wife"]]
        if person.get("husband"):
            per_instance.husband = Person.people[person["husband"]]

    return list(Person.people.values())
