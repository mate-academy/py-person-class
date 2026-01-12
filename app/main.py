class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list):
    Person.people.clear()
    result = [Person(p["name"], p["age"]) for p in people]

    for p in people:
        person = Person.people[p["name"]]
        if p.get("wife") is not None:
            person.wife = Person.people[p["wife"]]

        if p.get("husband") is not None:
            person.husband = Person.people[p["husband"]]

    return result
