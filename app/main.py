class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    need_return = []
    Person.people.clear()
    need_return = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        if (person.get("wife", "dont_have") != "dont_have"
                and not person["wife"] is None):
            Person.people[f"{person["name"]}"].wife \
                = Person.people[person["wife"]]
        if (person.get("husband", "dont_have") != "dont_have"
                and not person["husband"] is None):
            Person.people[f"{person["name"]}"].husband\
                = Person.people[person["husband"]]
    return need_return
