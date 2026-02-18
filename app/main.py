class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    new_persons = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        new_person = Person.people[person["name"]]
        if person.get("wife"):
            wife = Person.people[person["wife"]]
            new_person.wife = wife
        if person.get("husband"):
            husband = Person.people[person["husband"]]
            new_person.husband = husband

    return new_persons
