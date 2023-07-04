class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person = Person(person["name"], person["age"])
        person_list.append(person)

    for one_person in people:
        person = Person.people[one_person["name"]]
        if one_person.get("wife") is not None:
            person.wife = Person.people[one_person["wife"]]
        if one_person.get("husband") is not None:
            person.husband = Person.people[one_person["husband"]]
    return person_list
