class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person, details in zip(person_list, people):
        wife_name = details.get("wife")
        husband_name = details.get("husband")
        if wife_name is not None:
            person.wife = Person.people[wife_name]
        if husband_name is not None:
            person.husband = Person.people[husband_name]

    return person_list
