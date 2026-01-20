
class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = [Person(peep["name"], peep["age"]) for peep in people]
    for peep in people:
        person = Person.people[peep["name"]]
        wife_name = peep.get("wife")
        if wife_name is not None:
            person.wife = Person.people[peep["wife"]]
        husband_name = peep.get("husband")
        if husband_name is not None:
            person.husband = Person.people[peep["husband"]]

    return result
