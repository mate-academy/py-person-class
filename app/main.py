class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person_data["name"], person_data["age"]) for person_data in people]

    for spouse in people:
        person = Person.people[spouse["name"]]

        if wife := spouse.get("wife"):
            person.wife = Person.people[wife]
        elif husband := spouse.get("husband"):
            person.husband = Person.people[husband]

    return person_list
