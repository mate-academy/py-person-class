class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    person_instances = [Person(person["name"], person["age"])
                        for person in people]

    partner = ""
    for person in people:
        if person.get("wife", None):
            partner = person["wife"]
            Person.people[person["name"]].wife = Person.people[partner]
        elif person.get("husband", None):
            partner = person["husband"]
            Person.people[person["name"]].husband = Person.people[partner]

    return person_instances
