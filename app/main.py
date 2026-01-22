class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    [Person(person["name"], person["age"]) for person in people]
    for pers in people:
        wife_name = pers.get("wife")
        if wife_name is not None:
            Person.people[pers["name"]].wife = Person.people[wife_name]
        husband_name = pers.get("husband")
        if husband_name is not None:
            Person.people[pers["name"]].husband \
                = Person.people[husband_name]
    return list(Person.people.values())
