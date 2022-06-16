class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.people.update({f"{name}": self})


def create_person_list(people: list) -> list:
    ls = []
    for i in people:
        name = i["name"]
        age = i["age"]
        ls.append(Person(name, age))
    for pos, i in enumerate(people):
        if "wife" in i:
            if i["wife"] is not None:
                ls[pos].wife = Person.people[i["wife"]]
        if "husband" in i:
            if i["husband"] is not None:
                ls[pos].husband = Person.people[i["husband"]]
    return ls
