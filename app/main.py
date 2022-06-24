class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    if people:
        for member in people:
            person_list.append(Person(member["name"], member["age"]))

        for member in people:
            if "husband" in member.keys():
                if member["husband"] is not None:
                    Person.people[member["name"]].husband =\
                        Person.people[member["husband"]]

            if "wife" in member.keys():
                if member["wife"] is not None:
                    Person.people[member["name"]].wife = \
                        Person.people[member["wife"]]

    return person_list
