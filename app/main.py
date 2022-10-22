class Person:
    people = {}

    def __init__(self, name: str, age: int) -> dict:
        self.age = age
        self.name = name
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    res = []
    for i in people:
        person = Person(i["name"], i["age"])
        res.append(person)
    for person in people:
        if person.get("wife") is not None:
            Person.people[person.get("name")].wife = \
                Person.people[person.get("wife")]
        elif person.get("husband") is not None:
            Person.people[person.get("name")].husband = \
                Person.people[person.get("husband")]
    return res
