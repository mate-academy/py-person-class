class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.age = age
        self.name = name
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = []
    for person in people:
        people_list.append(Person(name=person["name"], age=person["age"]))
    for person in people:
        if "wife" in person:
            if person["wife"] is not None:
                person_wife = Person.people[person["wife"]]
                Person.people[person["name"]].wife = person_wife
        if "husband" in person:
            if person["husband"] is not None:
                person_husband = Person.people[person["husband"]]
                Person.people[person["name"]].husband = person_husband
    return people_list
