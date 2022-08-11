class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people.update({name: self})


def create_person_list(people: list) -> list:
    person_list = []
    for elements in people:
        person_list.append(Person(elements["name"], elements["age"]))
    for elements in people:
        if "wife" in elements and elements["wife"] is not None:
            Person.people[elements["name"]].wife = \
                Person.people[elements["wife"]]
        elif "husband" in elements and \
                elements["husband"] is not None:
            Person.people[elements["name"]].husband = \
                Person.people[elements["husband"]]

    return person_list
