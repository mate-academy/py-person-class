class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        tmp = Person(person["name"], person["age"])
        person_list.append(tmp)
    for person in people:
        if "wife" in person and person["wife"] is not None:
            link_to_wife = Person.people[person["wife"]]
            Person.people[person["name"]].wife = link_to_wife
        elif "husband" in person and person["husband"] is not None:
            link_to_husband = Person.people[person["husband"]]
            Person.people[person["name"]].husband = link_to_husband
    return person_list
