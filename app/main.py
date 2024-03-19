
class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    list_person = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        if "wife" in person and person["wife"] is not None:
            his_wife = Person.people[person["wife"]]
            Person.people[person["name"]].wife = his_wife
        if "husband" in person and person["husband"] is not None:
            her_husband = Person.people[person["husband"]]
            Person.people[person["name"]].husband = her_husband

    return list_person
