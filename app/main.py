class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_person = []
    for person in people:
        human = Person(person["name"], person["age"])
        list_person.append(human)
    for ind in range(len(list_person)):
        if "wife" in people[ind] and people[ind]["wife"] is not None:
            list_person[ind].wife = Person.people[people[ind]["wife"]]
        if "husband" in people[ind] and people[ind]["husband"] is not None:
            list_person[ind].husband = Person.people[people[ind]["husband"]]
    return list_person
