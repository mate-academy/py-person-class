class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()

    for person_d in people:
        Person(person_d["name"], person_d["age"])

    for person_d in people:
        person = Person.people[person_d["name"]]
        if person_d.get("wife"):
            person.wife = Person.people.get(person_d["wife"])
        if person_d.get("husband"):
            person.husband = Person.people.get(person_d["husband"])

    return [Person.people[person_d["name"]] for person_d in people]
