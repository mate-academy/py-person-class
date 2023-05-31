class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        name = person.get("name")
        age = person.get("age")
        human = Person(name, age)
        person_list.append(human)
    for partner in people:
        if partner.get("wife") is not None:
            name_partner = partner.get("wife")
            Person.people[partner["name"]].wife\
                = Person.people[name_partner]
        elif partner.get("husband") is not None:
            name_partner = partner.get("husband")
            Person.people[partner["name"]].husband\
                = Person.people[name_partner]
    return person_list
