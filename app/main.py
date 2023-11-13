class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    out = []

    for person in people:
        out.append(Person(person["name"], person["age"]))

    all_p = Person.people

    for i, data in enumerate(people):
        if ("wife" in data) and (data["wife"] is not None):
            out[i].wife = all_p[data["wife"]]

        if ("husband" in data) and (data["husband"] is not None):
            out[i].husband = all_p[data["husband"]]

    print("out", out)
    return out
