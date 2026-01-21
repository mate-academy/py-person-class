class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    persons_list = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        name = person["name"]
        if person.get("wife"):
            Person.people[name].wife = Person.people[person["wife"]]
        elif person.get("husband"):
            Person.people[name].husband = Person.people[person["husband"]]
    return persons_list
