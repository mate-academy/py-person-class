class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        new_person = Person(person["name"], person["age"])
        person_list.append(new_person)

    for ind in people:
        if ind.get("wife"):
            Person.people[ind["name"]].wife = Person.people[ind["wife"]]
        elif ind.get("husband"):
            Person.people[ind["name"]].husband = Person.people[ind["husband"]]

    return person_list
