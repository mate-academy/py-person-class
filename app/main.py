class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def create_person_list(some_people: list) -> list:
    Person.people = {}
    result = []
    for person in some_people:
        Person.people[person["name"]] = Person(person["name"], person["age"])

    for person in some_people:
        current_person = Person.people[person["name"]]
        if person.get("wife") and person["wife"] in Person.people:
            current_person.wife = Person.people[person["wife"]]
        if person.get("husband") and person["husband"] in Person.people:
            current_person.husband = Person.people[person["husband"]]
        result.append(Person.people[person["name"]])
    return result
