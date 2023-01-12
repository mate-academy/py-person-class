class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    new_list = [
        Person(single_prs["name"], single_prs["age"])
        for single_prs in people
    ]
    for person in people:
        if "wife" in person and person["wife"] is not None:
            wife = Person.people[person["wife"]]
            Person.people[person["name"]].wife = wife
        elif "husband" in person and person["husband"] is not None:
            husband = Person.people[person["husband"]]
            Person.people[person["name"]].husband = husband
        continue

    return new_list
