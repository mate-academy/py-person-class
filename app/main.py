class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:
    person_list = []
    for man in people:
        person = Person(man["name"], man["age"])
        person_list.append(person)
        Person.people[man["name"]] = person
    for man in people:
        if "wife" in man:
            if not man["wife"] is None:
                Person.people[man["name"]].wife = Person.people[man["wife"]]
        if "husband" in man:
            if not man["husband"] is None:
                husband = Person.people[man["husband"]]
                Person.people[man["name"]].husband = husband

    return person_list
