class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(i["name"], i["age"]) for i in people]

    for i in people:
        if "wife" in i and i["wife"] is not None:
            Person.people[i["name"]].wife = Person.people[i["wife"]]

        elif "husband" in i and i["husband"] is not None:
            Person.people[i["name"]].husband = Person.people[i["husband"]]

    return person_list
