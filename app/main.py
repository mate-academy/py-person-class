class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for man in people:
        person_list.append(Person(man["name"], man["age"]))

    for man in people:
        if "wife" in man:
            if man["wife"]:
                person_list[people.index(man)].wife \
                    = Person.people[people[people.index(man)]["wife"]]
        if "husband" in man:
            if man["husband"]:
                person_list[people.index(man)].husband \
                    = Person.people[people[people.index(man)]["husband"]]

    return person_list
