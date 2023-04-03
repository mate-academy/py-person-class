class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:

    person_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        if person.get("wife"):
            husband = Person.people[person["name"]]
            husband.wife = Person.people[person["wife"]]
        elif person.get("husband"):
            wife = Person.people[person["name"]]
            wife.husband = Person.people[person["husband"]]

    return person_list
