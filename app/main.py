class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        human = Person.people[person["name"]]

        if "husband" in person and person["husband"]:
            add_husband = Person.people[person["husband"]]
            setattr(human, "husband", add_husband)

        elif "wife" in person and person["wife"]:
            add_wife = Person.people[person["wife"]]
            setattr(human, "wife", add_wife)

    return result
