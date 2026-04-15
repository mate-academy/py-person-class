class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(p["name"], p["age"]) for p in people]
    persons = Person.people
    for person in people:
        if person.get("wife") is not None:
            persons[person["name"]].wife = persons[person["wife"]]
        elif person.get("husband") is not None:
            persons[person["name"]].husband = persons[person["husband"]]
    return person_list
