class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    for person in people:
        Person(person["name"], person["age"])
    for person in people:
        persons = Person.people[person["name"]]
        if "wife" in person and person["wife"] is not None:
            persons.wife = Person.people[person["wife"]]
        elif "husband" in person and person["husband"] is not None:
            persons.husband = Person.people[person["husband"]]

    return [Person.people[person["name"]] for person in people]
