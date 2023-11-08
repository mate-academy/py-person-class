class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list:

    people_list = [Person(i["name"], i["age"]) for i in people]
    for i in people:
        if i.get("wife"):
            Person.people[i["name"]].wife = Person.people[i["wife"]]
        if i.get("husband"):
            Person.people[i["name"]].husband = Person.people[i["husband"]]
    return people_list
