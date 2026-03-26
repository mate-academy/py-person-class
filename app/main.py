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

    for il, pl in enumerate(people):
        wife_name = pl.get("wife")
        if wife_name is not None:
            person_list[il].wife = Person.people[wife_name]
        husband_name = pl.get("husband")
        if husband_name is not None:
            person_list[il].husband = Person.people[husband_name]
    return person_list
