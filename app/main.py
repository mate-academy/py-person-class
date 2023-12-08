class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    created_person_list = [
        Person(people_data.get("name"), people_data.get("age"))
        for people_data in people
    ]

    for person in people:
        person_object = Person.people[person["name"]]
        if person.get("wife"):
            person_object.wife = Person.people[person["wife"]]

        if person.get("husband"):
            person_object.husband = Person.people[person["husband"]]

    return created_person_list
