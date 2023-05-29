class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    @classmethod
    def get_person(cls, name: str) -> "Person":
        return cls.people.get(name)


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        name = person["name"]
        age = person["age"]
        Person(name, age)
    for person in people:
        new_person = Person.get_person(person["name"])
        if "wife" in person and person["wife"] is not None:
            new_person.wife = Person.people[person["wife"]]
            Person.people[person["wife"]].husband = new_person
        if "husband" in person and person["husband"] is not None:
            new_person.husband = Person.people[person["husband"]]
        person_list.append(new_person)
    return person_list
