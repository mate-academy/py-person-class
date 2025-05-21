class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    person_dicts = []
    for person_dict in people:
        person = Person(person_dict["name"], person_dict["age"])
        person_dicts.append(person_dict)
        person_list.append(person)

    for person, person_dict in zip(person_list, person_dicts):
        if "wife" in person_dict and person_dict["wife"] is not None:
            person.wife = Person.people.get(person_dict["wife"])
        elif "husband" in person_dict and person_dict["husband"] is not None:
            person.husband = Person.people.get(person_dict["husband"])

    return person_list
