class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:

        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person in people:
        person_obj = Person(person["name"], person["age"])
        person_list.append(person_obj)

    for creature in people:
        person_obj = Person.people[creature["name"]]

        if ("wife" in creature) and (creature["wife"] is not None):
            person_obj.wife = Person.people[creature["wife"]]

        elif ("husband" in creature) and (creature["husband"] is not None):
            person_obj.husband = Person.people[creature["husband"]]

    return person_list
