class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    for person in people:
        Person(person["name"], person["age"])
    add_para_to_person(people)
    return list(Person.people.values())


def add_para_to_person(people: list) -> None:
    for person in people:
        if "wife" in person.keys() and person["wife"] is not None:
            single_person = Person.people[person["name"]]
            wife = Person.people[person["wife"]]
            single_person.wife = wife
        if "husband" in person.keys() and person["husband"] is not None:
            single_person = Person.people[person["name"]]
            husband = Person.people[person["husband"]]
            single_person.husband = husband
