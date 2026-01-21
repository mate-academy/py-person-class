class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    for person in people:
        Person(person["name"], person["age"])
    add_partner_to_person(people)
    return list(Person.people.values())


def add_partner_to_person(people: list) -> None:
    for person in people:
        single_person = Person.people[person["name"]]
        if person.get("wife") is not None:
            wife = Person.people[person["wife"]]
            single_person.wife = wife
        if person.get("husband") is not None:
            husband = Person.people[person["husband"]]
            single_person.husband = husband
