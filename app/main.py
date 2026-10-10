class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person_list.append(Person(person["name"], person["age"]))
        if "wife" in person and person["wife"] in Person.people:
            person_list[-1].wife = Person.people[person["wife"]]
            Person.people[person["wife"]].husband = person_list[-1]
        if "husband" in person and person["husband"] in Person.people:
            person_list[-1].husband = Person.people[person["husband"]]
            Person.people[person["husband"]].wife = person_list[-1]
    return person_list
