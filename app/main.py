class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        obj = Person(person["name"], person["age"])
        Person.people[person["name"]] = obj
        result.append(obj)

    for person in people:
        person_name = person["name"]
        if "wife" in person and person["wife"] is not None:
            (setattr
             (Person.people[person_name],
              "wife",
              Person.people[person["wife"]]))
        if "husband" in person and person["husband"] is not None:
            (setattr
             (Person.people[person_name],
              "husband",
              Person.people[person["husband"]]))

    return result
