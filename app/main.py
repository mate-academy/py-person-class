class Person:
    people = {}
    def __init__(self, name: str, age:int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}

    for person_dict in people:
        Person(person_dict["name"], person_dict["age"])
    for person_dict in people:
        p = Person.people[person_dict["name"]]
        if "wife" in person_dict and person_dict["wife"] is not None:
            p.wife = Person.people[person_dict["wife"]]
        if "husband" in person_dict and person_dict["husband"] is not None:
            p.husband = Person.people[person_dict["husband"]]

    return list(Person.people.values())

