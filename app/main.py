class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list[dict]) -> list:
    person_list = [
        Person(person["name"], person["age"]) for person in people
    ]

    for person in people:
        person_name = person["name"]
        person_object = Person.people[person_name]

        if person.get("wife"):
            person_object.wife = Person.people[person["wife"]]
        elif person.get("husband"):
            person_object.husband = Person.people[person["husband"]]

    return person_list
