class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [
        (Person(person_data["name"], person_data["age"]))
        for person_data in people
    ]

    for human in people:
        person = Person.people[human["name"]]
        if human.get("wife"):
            person.wife = Person.people[human["wife"]]
        if human.get("husband"):
            person.husband = Person.people[human["husband"]]

    return person_list
