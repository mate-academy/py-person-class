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

    for i in range(len(people)):
        if "wife" in people[i]:
            if people[i]["wife"]:
                person_list[i].wife = Person.people[people[i]["wife"]]
        if "husband" in people[i]:
            if people[i]["husband"]:
                person_list[i].husband = Person.people[people[i]["husband"]]

    return person_list
