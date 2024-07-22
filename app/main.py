class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = []
    if not people:
        return persons

    for i, person in enumerate(people):
        persons.append(Person(person["name"], person["age"]))
        if person.get("wife"):
            persons[i].wife = person["wife"]
        elif (person.get("husband")
              and not person["husband"].startswith("None")):
            persons[i].husband = person["husband"]

    return persons
