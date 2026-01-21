class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        new_person = Person(person["name"], person["age"])
        result.append(new_person)

    for person in people:
        person_ref = Person.people[person["name"]]
        if person.get("wife"):
            person_ref.wife = Person.people.get(person["wife"])
        if person.get("husband"):
            person_ref.husband = Person.people.get(person["husband"])
    return result
