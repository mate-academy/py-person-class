class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(
            name=person_dict["name"],
            age=person_dict["age"])
        for person_dict in people
    ]
    for person in people:
        person_instance = Person.people[person["name"]]
        if person.get("wife") is not None:
            person_instance.wife = Person.people[person["wife"]]
        if person.get("husband") is not None:
            person_instance.husband = Person.people[person["husband"]]

    return person_list
