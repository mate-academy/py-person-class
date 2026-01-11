class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_list = [
        Person(
            name=person.get("name"), age=person.get("age")
        ) for person in people
    ]

    for i, person in enumerate(people):
        current = people_list[i]
        if person.get("wife"):
            wife_name = person.get("wife")
            current.wife = Person.people[wife_name]

        elif person.get("husband"):
            husband_name = person.get("husband")
            current.husband = Person.people[husband_name]

    return people_list
