class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    person_list = [Person(person["name"], person["age"]) for person in people]

    for i, person in enumerate(people):
        current_person = person_list[i]

        if "wife" in person and person["wife"] is not None:
            wife_name = person["wife"]
            current_person.wife = Person.people[wife_name]

        if "husband" in person and person["husband"] is not None:
            husband_name = person["husband"]
            current_person.husband = Person.people[husband_name]

    return person_list
