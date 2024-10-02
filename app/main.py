class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    people_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        if wife := person.get("wife"):
            Person.people[person["name"]].wife = Person.people[wife]
        elif husband := person.get("husband"):
            Person.people[person["name"]].husband = Person.people[husband]

    return people_list
