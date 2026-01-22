class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people_list: list) -> list:
    res = []
    Person.people = {}

    for person in people_list:
        res.append(Person(person["name"], person["age"]))

    for person in people_list:
        if "wife" in person.keys() and not (person["wife"] is None):
            wife_reference = Person.people[person["wife"]]
            Person.people[person["name"]].wife = wife_reference
        elif "husband" in person.keys() and not (person["husband"] is None):
            husband_reference = Person.people[person["husband"]]
            Person.people[person["name"]].husband = husband_reference

    return res
