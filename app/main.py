class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for spouse in people:
        if spouse.get("wife"):
            wife = Person.people[spouse["wife"]]
            wife.husband = Person.people[spouse["name"]]
        if spouse.get("husband"):
            husband = Person.people[spouse["husband"]]
            husband.wife = Person.people[spouse["name"]]

    return person_list
