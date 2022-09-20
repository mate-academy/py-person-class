class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[dict]:
    #
    for person in people:
        Person(person["name"], person["age"])
    #
    for person in people:
        if "wife" in person and person["wife"]:
            Person.people[person["name"]].wife =\
                Person.people[person["wife"]]
        if "husband" in person and person["husband"]:
            Person.people[person["name"]].husband = \
                Person.people[person["husband"]]
    #
    return list(Person.people.values())
