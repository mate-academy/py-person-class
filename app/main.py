class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    res = []
    for hum in people:
        person = Person(name=hum["name"], age=hum["age"])
        res.append(person)

    for hum in people:
        person = Person.people[hum["name"]]
        if hum.get("wife", None):
            person.wife = Person.people[hum["wife"]]
        elif hum.get("husband", None):
            person.husband = Person.people[hum["husband"]]
    return res
