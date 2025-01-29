class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list[Person]:
    persons = [Person(person["name"], person["age"]) for person in people]
    for ind, person in zip(people, persons):
        if ind.get("wife"):
            person.wife = Person.people.get(ind["wife"])
        elif ind.get("husband"):
            person.husband = Person.people.get(ind["husband"])
    return persons
