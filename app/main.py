class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def set_partner(person_dict: dict) -> None:
    person = Person.people[person_dict["name"]]
    if "wife" in person_dict:
        if person_dict["wife"]:
            person.wife = Person.people[person_dict["wife"]]
    elif "husband" in person_dict:
        if person_dict["husband"]:
            person.husband = Person.people[person_dict["husband"]]


def create_person_list(people: list) -> list[Person]:
    persons_list: list[Person] = \
        [Person(person["name"], person["age"]) for person in people]
    for person in people:
        set_partner(person)
    return persons_list
