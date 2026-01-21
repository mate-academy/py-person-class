class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for i in range(len(people)):
        if "wife" in people[i] and people[i]["wife"] is not None:
            for name_of_partner in Person.people.keys():
                if name_of_partner == people[i]["wife"]:
                    person_list[i].wife = Person.people[name_of_partner]
        if "husband" in people[i] and people[i]["husband"] is not None:
            for name_of_partner in Person.people.keys():
                if name_of_partner == people[i]["husband"]:
                    person_list[i].husband = Person.people[name_of_partner]

    return person_list
