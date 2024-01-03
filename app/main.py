class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    result = list()

    for person in people:
        Person(person["name"], person["age"])

    for person in people:
        tmp = Person.people[person["name"]]
        if "wife" in person:
            if person["wife"]:
                tmp.wife = Person.people[person["wife"]]
        elif "husband" in person:
            if person["husband"]:
                tmp.husband = Person.people[person["husband"]]
        result.append(tmp)

    return result
