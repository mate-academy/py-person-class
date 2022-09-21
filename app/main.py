class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        name = person["name"]

        if "wife" in person:
            wife = person["wife"]
            if wife is not None:
                Person.people[name].wife = Person.people[wife]

        elif "husband" in person:
            husband = person["husband"]
            if husband is not None:
                Person.people[name].husband = Person.people[husband]

    return person_list
