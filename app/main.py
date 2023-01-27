class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:
    person_list = [Person(name=i["name"], age=i["age"]) for i in people]
    Person.people = {exemplar.name: exemplar for exemplar in person_list}

    for man in people:
        if man.get("wife") is not None:
            Person.people[man["name"]].wife = Person.people[man["wife"]]
        if man.get("husband") is not None:
            Person.people[man["name"]].husband = Person.people[man["husband"]]
    return person_list
