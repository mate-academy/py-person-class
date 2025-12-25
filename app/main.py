class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    objects = []
    for dictionary in people:
        person_new = Person(name=dictionary["name"], age=dictionary["age"])
        objects.append(person_new)
    for index in range(len(people)):
        if "wife" in people[index].keys() and \
                people[index]["wife"] in Person.people:
            objects[index].wife = Person.people[people[index]["wife"]]
        if "husband" in people[index].keys() and \
                people[index]["husband"] in Person.people:
            objects[index].husband = Person.people[people[index]["husband"]]
    return objects
