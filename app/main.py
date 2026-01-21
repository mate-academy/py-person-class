class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people = {}
    new_list_person = []
    for person in people:
        new_list_person.append(Person(person["name"], person["age"]))
    for married in people:
        person_married = Person.people[married["name"]]
        if "wife" in married and married["wife"] is not None:
            person_married.wife = Person.people[married["wife"]]
        if "husband" in married and married["husband"] is not None:
            person_married.husband = Person.people[married["husband"]]
    return new_list_person
