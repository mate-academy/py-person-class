class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    for person in people:
        new_person = Person(person["name"], person["age"])
        Person.people[new_person.name] = new_person

    person_list = []
    for person in people:
        lookup = Person.people[person["name"]]
        if person.get("wife") is not None:
            wife = Person.people[person["wife"]]
            lookup.wife = wife
        if person.get("husband") is not None:
            husband = Person.people[person["husband"]]
            lookup.husband = husband
        person_list.append(lookup)
    return person_list
