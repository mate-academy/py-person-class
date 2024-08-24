class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_list = [Person(person["name"], person["age"]) for person in people]

    for person_dict in people:
        person = Person.people[person_dict["name"]]

        if person_dict.get("wife", False):
            person.wife = Person.people[person_dict["wife"]]
        elif person_dict.get("husband", False):
            person.husband = Person.people[person_dict["husband"]]

    return people_list
