class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person_list.append(Person(person["name"], person["age"]))
        if "wife" in person and person["wife"] in Person.people:
            Person.people[person["name"]].wife\
                = Person.people[person["wife"]]
            Person.people[person["name"]].wife.husband\
                = Person.people[person["name"]]
        if "husband" in person and person["husband"] in Person.people:
            Person.people[person["name"]].husband\
                = Person.people[person["husband"]]
            Person.people[person["name"]].husband.wife\
                = Person.people[person["name"]]
    return person_list
