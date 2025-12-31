class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    new_persons = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        person_data = Person.people[person["name"]]
        if person.get("wife"):
            person_data.wife = Person.people[person["wife"]]
        if person.get("husband"):
            person_data.husband = Person.people[person["husband"]]

    return new_persons
