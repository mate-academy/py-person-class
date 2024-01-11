
class Person:
    people = {}

    def __init__(self,
                 name: str,
                 age: int,
                 ) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        human = Person(name=person["name"],
                       age=person["age"],)
        person_list.append(human)

    for person in people:
        human = Person.people[person["name"]]
        if "wife" in person:
            if person["wife"]:
                human.wife = Person.people[person["wife"]]
        elif "husband" in person:
            if person["husband"]:
                human.husband = Person.people[person["husband"]]
    return person_list
