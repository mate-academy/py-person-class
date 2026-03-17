class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    list_p = [Person(person["name"], person["age"]) for person in people]

    for people_dict, person in zip(people, list_p):
        if people_dict.get("wife") is not None:
            person.wife = Person.people[people_dict.get("wife")]
        if people_dict.get("husband") is not None:
            person.husband = Person.people[people_dict.get("husband")]

    return list_p
