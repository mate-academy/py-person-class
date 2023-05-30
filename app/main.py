class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person_list.append(Person(name=person["name"], age=person["age"]))

    for person in people:
        if person.get("wife"):
            person_wife = Person.people[person["wife"]]
            Person.people[person["name"]].wife = person_wife

        if person.get("husband"):
            person_husband = Person.people[person["husband"]]
            Person.people[person["name"]].husband = person_husband

    return person_list
