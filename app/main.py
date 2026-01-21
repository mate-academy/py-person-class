class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        prs = Person.people[person["name"]]
        if person.get("wife"):
            prs.wife = Person.people[person["wife"]]
        if person.get("husband"):
            prs.husband = Person.people[person["husband"]]
        else:
            continue
    return person_list
