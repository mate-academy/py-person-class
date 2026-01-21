class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person_list.append(Person(person["name"], person["age"]))
    for i, person in enumerate(people):
        if person.get("wife") is not None:
            person_list[i].wife = Person.people.get(person["wife"])
        elif person.get("husband") is not None:
            person_list[i].husband = Person.people.get(person["husband"])
    return person_list
