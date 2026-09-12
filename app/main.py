class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        name, age = person["name"], person["age"]
        person_list.append(Person(name, age))
    for person in people:
        pers = Person.people[person["name"]]
        if person.get("wife"):
            pers.wife = Person.people[person["wife"]]
        elif person.get("husband"):
            pers.husband = Person.people[person["husband"]]
    return person_list
