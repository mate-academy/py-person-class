class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    list_person = []
    for one_person in people:
        person = Person(name=one_person["name"], age=one_person["age"])
        list_person.append(person)
    for one in people:
        if "wife" in one and one["wife"] is not None:
            Person.people[one["name"]].wife = Person.people[one["wife"]]
        if "husband" in one and one["husband"] is not None:
            Person.people[one["name"]].husband = Person.people[one["husband"]]
    return list_person
