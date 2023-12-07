class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    for specimen in people:
        Person(specimen["name"], specimen["age"])
    for specimen_2 in people:
        if "wife" in specimen_2 and specimen_2["wife"] in Person.people:
            Person.people[specimen_2["name"]].wife =\
                Person.people[specimen_2["wife"]]
        elif ("husband" in specimen_2
              and specimen_2["husband"] in Person.people):
            Person.people[specimen_2["name"]].husband = (
                Person.people)[specimen_2["husband"]]
    return list(Person.people.values())
