class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = []
    for person in people:
        people_list.append(Person(name=person["name"], age=person["age"]))
    for person in people:
        name = person["name"]
        if "wife" in person and person["wife"] in Person.people:
            Person.people[name].wife = Person.people[person["wife"]]
        elif "husband" in person and person["husband"] in Person.people:
            Person.people[name].husband = Person.people[person["husband"]]
    return people_list
