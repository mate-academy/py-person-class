class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = [Person(person["name"], person["age"]) for person in people]
    for person in zip(people, result):
        wife_name = person[0].get("wife")
        if wife_name is not None:
            person[1].wife = Person.people[wife_name]
        husband_name = person[0].get("husband")
        if husband_name is not None:
            person[1].husband = Person.people[husband_name]
    return result
