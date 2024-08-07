class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        persons = Person.people
        if person.get("wife") is not None:
            persons[person["name"]].wife = persons[person["wife"]]
            continue
        if person.get("husband") is not None:
            persons[person["name"]].husband = persons[person["husband"]]
    return person_list
