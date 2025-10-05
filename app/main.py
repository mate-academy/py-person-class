class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    list_of_persons = []
    for person in people:
        person = Person(person["name"], person["age"])
        list_of_persons.append(person)
    for person in people:
        data = Person.people[person["name"]]
        if "wife" in person and person["wife"] is not None:
            data.wife = Person.people.get(person["wife"])
        if "husband" in person and person["husband"] is not None:
            data.husband = Person.people.get(person["husband"])
    return list_of_persons
