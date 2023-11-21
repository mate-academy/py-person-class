class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    p_inst = []
    [p_inst.append(Person(person["name"], person["age"])) for person in people]

    for person in people:
        person_list = Person.people[person["name"]]
        if person.get("wife"):
            person_list.wife = Person.people[person["wife"]]
        if person.get("husband"):
            person_list.husband = Person.people[person["husband"]]

    return p_inst
