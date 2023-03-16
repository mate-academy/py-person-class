class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = list()
    for person in people:
        name = person["name"]
        age = person["age"]
        new_person = Person(name, age)
        person_list.append(new_person)
    for person in people:
        if person.get("wife"):
            Person.people[person["name"]].wife = Person.people[person["wife"]]
        if person.get("husband"):
            Person.people[person["name"]].husband = Person.people[person["husband"]]

    return person_list
