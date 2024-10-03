class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()

    person_list = []

    for person_dict in people:
        person = Person(name=person_dict["name"], age=person_dict["age"])
        person_list.append(person)

    for person_dict in people:
        person = Person.people[person_dict["name"]]
        if "wife" in person_dict and person_dict["wife"] is not None:
            person.wife = Person.people[person_dict["wife"]]
        elif hasattr(person, "wife"):
            delattr(person, "wife")

        if "husband" in person_dict and person_dict["husband"] is not None:
            person.husband = Person.people[person_dict["husband"]]
        elif hasattr(person, "husband"):
            delattr(person, "husband")

    return person_list
