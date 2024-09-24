class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(peopl: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in peopl]
    for person in person_list:
        for pers in peopl:
            if pers.get("husband") and pers["name"] == person.name:
                person.husband = Person.people[pers["husband"]]
            if pers.get("wife") and pers["name"] == person.name:
                person.wife = Person.people[pers["wife"]]
    return person_list
