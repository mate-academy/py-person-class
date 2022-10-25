class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for one_person in people:
        person = Person(one_person["name"], one_person["age"])
        person_list.append(person)

    for person in Person.people.values():
        for this_person in people:
            if person.name == this_person["name"]:
                if "husband" in this_person:
                    if this_person["husband"] is not None:
                        person.husband = Person.people[this_person["husband"]]
                elif "wife" in this_person:
                    if this_person["wife"] is not None:
                        person.wife = Person.people[this_person["wife"]]

    return person_list
