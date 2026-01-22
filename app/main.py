class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    list_of_persons = []
    for person in people:
        Person(person["name"], person["age"])

    for person in people:
        the_dude = Person.people[person["name"]]
        if "wife" in person and person["wife"] is not None:
            the_dude.wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"] is not None:
            the_dude.husband = Person.people[person["husband"]]
        list_of_persons.append(the_dude)
    return list_of_persons
