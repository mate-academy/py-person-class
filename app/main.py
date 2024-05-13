class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    for person in people:
        Person(
            person["name"], person["age"]
        )
    for person in people:
        prsn = Person.people[person["name"]]
        if person.get("wife"):
            wife = Person.people[person["wife"]]
            prsn.wife = wife
        elif person.get("husband"):
            husband = Person.people[person["husband"]]
            prsn.husband = husband
    return list(Person.people.values())
