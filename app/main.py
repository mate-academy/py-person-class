class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for dict_person in people:
        if dict_person.get("husband"):
            Person.people[dict_person["husband"]].wife = (
                Person.people)[dict_person["name"]]
        elif dict_person.get("wife"):
            Person.people[dict_person["wife"]].husband = (
                Person.people)[dict_person["name"]]
        continue

    return person_list
