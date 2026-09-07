class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    res = []
    for person in people:
        res.append(Person(person["name"], person["age"]))
    for person in people:
        instance = Person.people[person["name"]]
        if person.get("wife") is not None:
            instance.wife = Person.people[person["wife"]]
        if person.get("husband") is not None:
            instance.husband = Person.people[person["husband"]]
    return res
