class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for line in people:
        person_list.append(Person(line["name"], line["age"]))

    for person in people:
        if person.get("wife") is not None:
            Person.people[person["name"]].wife = Person.people[person["wife"]]
        if person.get("husband") is not None:
            Person.people[person["name"]].husband = \
                Person.people[person["husband"]]
    return person_list
