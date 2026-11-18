class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    persons = {}
    for prs in people:
        person = Person(prs["name"], prs["age"])
        persons[person.name] = person
    for prs in people:
        if "wife" in prs and prs["wife"] is not None:
            persons[prs["name"]].wife = persons[prs["wife"]]
        if "husband" in prs and prs["husband"] is not None:
            persons[prs["name"]].husband = persons[prs["husband"]]
    return list(persons.values())
