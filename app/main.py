class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    res = [Person(person.get("name"),
                  person.get("age")) for person in people]
    for i in range(len(people)):
        if people[i].get("wife"):
            res[i].wife = Person.people.get(people[i].get("wife"))
        if people[i].get("husband"):
            res[i].husband = Person.people.get(people[i].get("husband"))
    return res
