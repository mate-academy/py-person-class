class Person:

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    people = {}


def create_person_list(people: list) -> list:
    result = []
    for pers in people:
        obj = Person(pers["name"], pers["age"])
        Person.people[pers["name"]] = obj
        result.append(obj)

    for el in people:
        person_name = el["name"]
        if "wife" in el and el["wife"] is not None:
            (setattr
             (Person.people[person_name],
              "wife",
              Person.people[el["wife"]]))
        if "husband" in el and el["husband"] is not None:
            (setattr
             (Person.people[person_name],
              "husband",
              Person.people[el["husband"]]))

    return result
