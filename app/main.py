class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = dict()

    person_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        if person.get("wife"):
            wife = Person.people[person["wife"]]
            Person.people[person["name"]].wife = wife
        if person.get("husband"):
            husband = Person.people[person["husband"]]
            Person.people[person["name"]].husband = husband

    return person_list
