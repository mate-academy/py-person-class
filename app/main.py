class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:

    list_of_people1 = [
        Person(person["name"], person["age"])
        for person in people
    ]

    for person in people:
        if person.get("wife"):
            current_person = Person.people[person["name"]]
            current_person.wife = Person.people[person["wife"]]
        elif person.get("husband"):
            current_person = Person.people[person["name"]]
            current_person.husband = Person.people[person["husband"]]

    return list_of_people1
