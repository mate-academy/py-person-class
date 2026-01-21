class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        Person(person["name"], person["age"])
        result.append(Person(person["name"], person["age"]))
    for person in people:
        name_of_person = Person.people[person["name"]]
        if "wife" in person and person["wife"]\
                and person["wife"] in Person.people:
            name_of_person.wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"]\
                and person["husband"] in Person.people:
            name_of_person.husband = Person.people[person["husband"]]
    return result
