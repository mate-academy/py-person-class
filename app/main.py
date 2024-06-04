class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    print(Person.people)
    for person in people:
        if "wife" in person and person["wife"]:
            if person["wife"] in Person.people:
                Person.people[person["name"]].wife \
                    = Person.people[person["wife"]]
        if "husband" in person and person["husband"]:
            if person["husband"] in Person.people:
                Person.people[person["name"]].husband \
                    = Person.people[person["husband"]]

    return person_list
