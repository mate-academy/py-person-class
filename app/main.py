class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        name, age = person["name"], person["age"]
        Person(name, age)
    for person in people:
        new_person = Person.people[person["name"]]
        if "wife" in person:
            if person["wife"] in Person.people:
                new_person.wife = Person.people[person["wife"]]
        if "husband" in person:
            if person["husband"] in Person.people:
                new_person.husband = Person.people[person["husband"]]
        result.append(new_person)
    for person in result:
        print(person)
    return result
