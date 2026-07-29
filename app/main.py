class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    lists = []
    for el in people:
        objects = Person(el["name"], el["age"])
        lists.append(objects)
    for el in people:
        if "wife" in el:
            if el["wife"] is not None:
                Person.people[el["name"]].wife = Person.people[el["wife"]]
        if "husband" in el:
            if el["husband"] is not None:
                Person.people[el["name"]].husband = (
                    Person.people[el["husband"]]
                )
    return lists
