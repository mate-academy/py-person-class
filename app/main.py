class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:
    person_list = []

    for person in people:
        person_list.append(Person(person["name"], person["age"]))
        Person.people[person["name"]] = person_list[-1]

    for person in people:
        if person.get("wife"):
            Person.people[person["name"]].wife = Person.people[person["wife"]]

        if person.get("husband"):
            Person.people[person["name"]].husband = (
                Person.people[person["husband"]]
            )

    return person_list
