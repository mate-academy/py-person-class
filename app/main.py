class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        if person.get("wife"):
            wife = Person.people[person["wife"]]
            husband = Person.people[person["name"]]
            husband.wife, wife.husband = wife, husband
    return people_list
