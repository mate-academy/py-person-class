
class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    new_person_list = [
        Person(person["name"], person["age"]) for person in people
    ]

    for person in people:
        main_person = Person.people[person["name"]]
        if person.get("wife"):
            person_wife = Person.people[person["wife"]]
            main_person.wife = person_wife
        elif person.get("husband"):
            person_husband = Person.people[person["husband"]]
            main_person.husband = person_husband

    return new_person_list
