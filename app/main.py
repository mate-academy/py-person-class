class Person:

    people = {}

    def __init__(self, name: str, age: float) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    res_list = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        if wife := person.get("wife"):
            Person.people[person["name"]].wife = res_list[person].wife
        elif husband := person.get("husband"):
            Person.people[person["name"]].husband = res_list[person].husband

    return res_list
