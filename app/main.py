class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person_temp = Person(person["name"], person["age"])
        person_list.append(person_temp)

    for person in people:
        if "wife" in person:
            if person["wife"] is not None:
                Person.people[person["name"]].wife = Person.people[person["wife"]]
        elif "husband" in person:
            if person["husband"] is not None:
                Person.people[person["name"]].husband = Person.people[person["husband"]]
    return person_list