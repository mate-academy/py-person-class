class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person_dict, person_obj in zip(people, person_list):
        if person_dict.get("wife"):
            person_obj.wife = Person.people[person_dict["wife"]]
        if person_dict.get("husband"):
            person_obj.husband = Person.people[person_dict["husband"]]

    return person_list
