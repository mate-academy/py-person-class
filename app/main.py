class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list[Person]:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        if husband := person.get("husband"):
            Person.people[person.get("name")].husband = Person.people[husband]
        if wife := person.get("wife"):
            Person.people[person.get("name")].wife = Person.people[wife]
    return person_list
