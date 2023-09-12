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

        if "wife" in person and person["wife"]:
            wife_to_add = Person.people[person["wife"]]
            setattr(human, "wife", wife_to_add)

        elif "husband" in person and person["husband"]:
            husband_to_add = Person.people[person["husband"]]
            setattr(human, "husband", husband_to_add)

    return result
