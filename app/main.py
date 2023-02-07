class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        Person(person["name"], person["age"])
    for el in people:
        if "husband" in el and not el["husband"] is None:
            Person.people[el["name"]].husband = Person.people[el["husband"]]
        if "wife" in el and not el["wife"] is None:
            Person.people[el["name"]].wife = Person.people[el["wife"]]
        person_list.append(Person.people[el["name"]])
    return person_list
