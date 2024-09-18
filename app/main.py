class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        Person(person["name"], person["age"])

    for person in people:
        if person.get("wife"):
            wife_name = person["wife"]
            Person.people[person["name"]].wife = Person.people[wife_name]
        if person.get("husband"):
            husband_name = person["husband"]
            Person.people[person["name"]].husband = Person.people[husband_name]

    for person in Person.people.values():
        person_list.append(person)

    return person_list
