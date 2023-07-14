class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    res = []
    for person in people:
        res.append(Person(person.get("name"), person.get("age")))
    for index in range(len(people)):
        if people[index].get("wife") is not None:
            res[index].wife = Person.people[people[index].get("wife")]
        if people[index].get("husband") is not None:
            res[index].husband = Person.people[people[index].get("husband")]
    return res
