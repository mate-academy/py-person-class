class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"],
                          person["age"]) for person in people]
    for i, person in enumerate(people):
        if person.get("wife"):
            person_list[i].wife = Person.people[person["wife"]]
        if person.get("husband"):
            person_list[i].husband = Person.people[person["husband"]]
    return person_list
