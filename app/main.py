class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({self.name: self})


def create_person_list(people: list[dict]) -> list:

    person_list = []

    for person in people:
        person = Person(person["name"], person["age"])
        person_list.append(person)

    for person in people:

        name = person["name"]

        if person.get("wife"):
            spouse_name = person["wife"]
            spouse = Person.people[spouse_name]
            Person.people[name].wife = spouse

        if person.get("husband"):
            spouse_name = person["husband"]
            spouse = Person.people[spouse_name]
            Person.people[name].husband = spouse

    return person_list
