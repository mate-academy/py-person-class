class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:

    person_list = [
        Person(name=person["name"], age=person["age"])
        for person in people
    ]

    for person_data in people:
        person = Person.people[person_data["name"]]

        if person_data.get("wife"):
            person.wife = Person.people[person_data["wife"]]

        if person_data.get("husband"):
            person.husband = Person.people[person_data["husband"]]

    return person_list
