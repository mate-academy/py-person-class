class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for one_person in people:
        person_list.append(
            Person(name=one_person["name"], age=one_person["age"])
        )
    for one_person in people:
        if "wife" in one_person and one_person["wife"] is not None:
            Person.people[one_person["name"]].wife = \
                Person.people[one_person["wife"]]
        if "husband" in one_person and one_person["husband"] is not None:
            Person.people[one_person["name"]].husband = \
                Person.people[one_person["husband"]]

    return person_list
