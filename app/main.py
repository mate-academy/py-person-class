class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(person["name"], person["age"]) for person in people
    ]

    for person, per in zip(people, person_list):
        wife_name = person.get("wife")
        husband_name = person.get("husband")

        if wife_name:
            per.wife = Person.people.get(wife_name)
        if husband_name:
            per.husband = Person.people.get(husband_name)

    return person_list
