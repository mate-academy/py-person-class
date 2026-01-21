class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        if person.get("wife"):
            link_to_wife = Person.people[person["wife"]]
            Person.people[person["name"]].wife = link_to_wife
        elif person.get("husband"):
            link_to_husband = Person.people[person["husband"]]
            Person.people[person["name"]].husband = link_to_husband
    return person_list
