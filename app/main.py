class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list[Person]:
    person_list = [Person(pers["name"], pers["age"]) for pers in people]
    for pers, person in zip(people, person_list):
        if "wife" in pers and pers["wife"]:
            person.wife = Person.people[pers["wife"]]
        elif "husband" in pers and pers["husband"]:
            person.husband = Person.people[pers["husband"]]
    return person_list
