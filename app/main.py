class Person:
    people = dict()

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = [Person(i["name"], i["age"]) for i in people]
    for i in people:
        if "wife" in i and i["wife"] is not None:
            Person.people[i["name"]].wife = Person.people[i["wife"]]
        if "husband" in i and i["husband"] is not None:
            Person.people[i["name"]].husband = Person.people[i["husband"]]
    return result
