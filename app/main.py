class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_people = [Person(person["name"], person["age"]) for person in people]
    for dict_person in people:
        person = Person.people[dict_person["name"]]

        if dict_person.get("wife", False):
            person.wife = Person.people[dict_person["wife"]]
        elif dict_person.get("husband", False):
            person.husband = Person.people[dict_person["husband"]]

    return list_people
