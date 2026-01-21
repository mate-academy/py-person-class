class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        if person["name"] not in Person.people:
            person_init = Person(person["name"], person["age"])
            Person.people[person["name"]] = person_init
            person_list.append(person_init)
    for person in people:
        person_init = Person.people[person["name"]]
        if "wife" in person.keys():
            if person["wife"] is None:
                person_init.wife = None
            else:
                person_init.wife = Person.people[person["wife"]]
        if "husband" in person.keys():
            if person["husband"] is None:
                person_init.husband = None
            else:
                person_init.husband = Person.people[person["husband"]]
    return person_list
