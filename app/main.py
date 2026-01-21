class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    lst = [Person(people_["name"], people_["age"]) for people_ in people]
    for i, people_ in enumerate(people):
        if "wife" in people_ and people_["wife"] is not None:
            lst[i].wife = Person.people[people_["wife"]]
        if people_.get("husband") and people_["husband"] is not None:
            lst[i].husband = Person.people[people_["husband"]]
    return lst
