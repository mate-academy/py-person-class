class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        # self.wife = None
        # self.husband = None
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for pers in people:
        person = Person(pers["name"], pers["age"])
        if pers.get("wife"):
            if pers["wife"] not in Person.people:
                Person.people[pers["wife"]] = Person(pers["wife"], None)
            person.wife = Person.people[pers["wife"]]
            person.wife.husband = person
        elif pers.get("husband"):
            if pers["husband"] not in Person.people:
                Person.people[pers["husband"]] = Person(pers["husband"], None)
            person.husband = Person.people[pers["husband"]]
            person.husband.wife = person
        person_list.append(person)
    return person_list
