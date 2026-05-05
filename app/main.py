class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_list = [Person(person["name"], person["age"]) for person in people]
    for person_dict in people:
        person_instance = Person.people[person_dict["name"]]
        if person_dict.get("wife"):
            person_instance.wife = Person.people[person_dict["wife"]]
        if person_dict.get("husband"):
            person_instance.husband = Person.people[person_dict["husband"]]
    return people_list
