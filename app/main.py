class Person:
    people = dict()

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    persons = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        obj = Person.people[person["name"]]

        if person.get("wife"):
            obj.wife = Person.people[person["wife"]]
        if person.get("husband"):
            obj.husband = Person.people[person["husband"]]
    return persons
