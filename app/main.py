class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    res = [
        Person(name=item.get("name"), age=item.get("age"))
        for item in people
    ]
    for i in range(len(people)):
        if wife := people[i].get("wife"):
            res[i].wife = Person.people.get(wife)
        elif husband := people[i].get("husband"):
            res[i].husband = Person.people.get(husband)
    return res
