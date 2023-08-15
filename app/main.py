class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(i["name"], i["age"]) for i in people]
    for i in people:
        if i.get("husband"):
            Person.people[i["name"]].husband = Person.people[i["husband"]]
        if i.get("wife"):
            Person.people[i["name"]].wife = Person.people[i["wife"]]
    return person_list
