class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = [
        Person(a_person["name"], a_person["age"])
        for a_person in people
    ]

    for a_person in people:
        result_person = Person.people[a_person["name"]]

        if a_person.get("wife"):
            result_person.wife = Person.people[a_person["wife"]]

        if a_person.get("husband"):
            result_person.husband = Person.people[a_person["husband"]]

    return result
