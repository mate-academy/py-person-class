class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    persons = [Person(person["name"], person["age"]) for person in people]
    for index, person in enumerate(people):
        if person.get("wife"):
            persons[index].wife = Person.people[person["wife"]]
        if person.get("husband"):
            persons[index].husband = Person.people[person["husband"]]
    return persons
