class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for pers in people:
        person = Person(pers["name"], pers["age"])
        person_list.append(person)
    for man in people:
        person = Person.people[man["name"]]
        wife_name = man.get("wife")
        if wife_name is not None:
            person.wife = Person.people[wife_name]
        husband_name = man.get("husband")
        if husband_name is not None:
            person.husband = Person.people[husband_name]
    return person_list
