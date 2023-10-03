class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    for person in people:
        Person(name=person["name"], age=person["age"])

    for person in people:
        if person[list(person.keys())[2]] is not None:
            if list(person.keys())[2] == "wife":
                Person.people[person["name"]].wife =\
                    Person.people[person[list(person.keys())[2]]]
            else:
                Person.people[person["name"]].husband =\
                    Person.people[person[list(person.keys())[2]]]
    return list(Person.people.values())
