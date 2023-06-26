class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    persons_list = [Person(person["name"], person["age"]) for person in people]

    for person, person_dict in zip(persons_list, people):
        if "wife" in person_dict and person_dict["wife"] is not None:
            person.wife = Person.people[person_dict["wife"]]
        elif "husband" in person_dict and person_dict["husband"] is not None:
            person.husband = Person.people[person_dict["husband"]]

    return persons_list
