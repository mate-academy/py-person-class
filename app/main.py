class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def add_wife(self, wife: str) -> None:
        for person_name in Person.people:
            if person_name == wife:
                self.wife = Person.people[person_name]
                Person.people[person_name].husband = self

    def add_husband(self, husband: str) -> None:
        for person_name in Person.people:
            if person_name == husband:
                self.husband = Person.people[person_name]
                Person.people[person_name].wife = self


def create_person_list(people: list) -> list:
    person_list = []
    for pl in people:
        if "wife" in pl:
            Person.people[pl["name"]] = Person(name=pl["name"], age=pl["age"])
            Person.people[pl["name"]].add_wife(pl["wife"])
        else:
            Person.people[pl["name"]] = Person(name=pl["name"], age=pl["age"])
            Person.people[pl["name"]].add_husband(pl["husband"])

        person_list.append(Person.people[pl["name"]])

    return person_list
