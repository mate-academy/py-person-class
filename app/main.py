class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    for person in people:
        Person(person["name"], person["age"])

    for person in people:
        if person.get("husband") is not None:
            husband = Person.people.get(person["husband"])
            if husband is not None:
                Person.people[person["name"]].husband = husband
        elif person.get("wife") is not None:
            wife = Person.people.get(person["wife"])
            if wife is not None:
                Person.people[person["name"]].wife = wife

    return list(Person.people.values())
