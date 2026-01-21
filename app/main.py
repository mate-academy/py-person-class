class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = []
    for human in people:
        person = Person(human["name"], human["age"])
        if "wife" in human and human["wife"] is not None:
            person.wife = human["wife"]
        if "husband" in human and human["husband"] is not None:
            person.husband = human["husband"]
        persons.append(person)

    for person in persons:
        make_marriage(person, "wife")
        make_marriage(person, "husband")
    return persons


def make_marriage(person: Person, role: str) -> None:
    if hasattr(person, role):
        setattr(person, role, Person.people[getattr(person, role)])
