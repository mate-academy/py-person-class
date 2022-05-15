class Person:
    people = {}

    def __init__(self, name, age, wife=None, husband=None):
        self.name = name
        self.age = age
        if wife is not None:
            self.wife = wife
        if husband is not None:
            self.husband = husband
        self.__class__.people[self.name] = self


def create_person_list(people: list) -> list:
    for person in people:
        Person(
            person["name"],
            person["age"],
            wife=person["wife"] if "wife" in person else None,
            husband=person["husband"] if "husband" in person else None
        )
    for person in people:
        if "wife" in person and person["wife"] is not None:
            Person.people[person["name"]].wife = \
                Person.people[person["wife"]]
        if "husband" in person and person["husband"] is not None:
            Person.people[person["name"]].husband = \
                Person.people[person["husband"]]
    return [Person.people[name] for name in Person.people]
