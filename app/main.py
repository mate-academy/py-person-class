class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    new_persons = [Person(person["name"], person["age"]) for person in people]

    for index, person in enumerate(people):
        if "wife" in person and person["wife"]:
            new_persons[index].wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"]:
            new_persons[index].husband = Person.people[person["husband"]]

    return new_persons
