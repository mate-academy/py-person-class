# main.py content

class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    for pers in people:
        Person(pers["name"], pers["age"])

    for pers in people:
        person = Person.people[pers["name"]]
        if "wife" in pers and pers["wife"]:
            wife_name = pers["wife"]
            wife = Person.people[wife_name]
            setattr(person, "wife", wife)
            setattr(wife, "husband", person)

    return list(Person.people.values())
