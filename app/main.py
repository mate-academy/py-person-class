class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(person_list: list) -> list:
    persons_instances = [Person(person["name"], person["age"])
                         for person in person_list]
    for person in person_list:
        if "wife" in person and person["wife"] is not None:
            Person.people[person["name"]].wife =\
                Person.people[person["wife"]]
        elif "husband" in person and person["husband"] is not None:
            Person.people[person["name"]].husband =\
                Person.people[person["husband"]]

    return persons_instances
