
class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}

    person_list = []

    for person in people:
        new_person = Person(person["name"], person["age"])
        person_list.append(new_person)

    for person, person_obj in zip(people, person_list):
        if person.get("wife") is not None:
            person_obj.wife = Person.people[person["wife"]]

        if person.get("husband") is not None:
            person_obj.husband = Person.people[person["husband"]]

    return person_list
