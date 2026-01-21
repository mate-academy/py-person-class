class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(person_dicts: list) -> list:
    persons = [Person(d["name"], d["age"]) for d in person_dicts]
    for pers in person_dicts:
        person = Person.people[pers["name"]]
        if "wife" in pers and pers["wife"]:
            person.wife = Person.people.get(pers["wife"])
        elif "husband" in pers and pers["husband"]:
            person.husband = Person.people.get(pers["husband"])
    return persons
