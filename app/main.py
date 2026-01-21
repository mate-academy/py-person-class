class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(name=person["name"], age=person["age"])
        for person in people
    ]

    for person_dict in people:
        person_obj = Person.people[person_dict["name"]]
        if person_dict.get("wife") is not None:
            person_obj.wife = Person.people[person_dict["wife"]]

        if person_dict.get("husband") is not None:
            person_obj.husband = Person.people[person_dict["husband"]]

    return person_list
