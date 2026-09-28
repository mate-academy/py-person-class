class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        new_person = Person(person["name"], person["age"])
        result.append(new_person)

    for person in people:
        if "wife" in person:
            Person.people[person["name"]].wife = Person.people[person["wife"]]

        elif "husband" in person:
            Person.people[person["name"]].husband \
                = Person.people[person["husband"]]

    return result
