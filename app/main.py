class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def add_wife(self, wife: str) -> None:
        self.wife = Person.people[wife]
        Person.people[wife].husband = self

    def add_husband(self, husband: str) -> None:
        self.husband = Person.people[husband]
        Person.people[husband].wife = self


def create_person_list(people: list) -> list:
    person_list = []
    for pl in people:
        if "wife" in pl:
            Person.people[pl["name"]] = Person(name=pl["name"], age=pl["age"])
            if pl["wife"] in Person.people:
                Person.people[pl["name"]].add_wife(pl["wife"])
        else:
            Person.people[pl["name"]] = Person(name=pl["name"], age=pl["age"])
            if pl["husband"] in Person.people:
                Person.people[pl["name"]].add_husband(pl["husband"])

        person_list.append(Person.people[pl["name"]])

    return person_list
