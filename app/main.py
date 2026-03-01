class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    result = [
        Person(person_dict["name"], person_dict["age"])
        for person_dict in people
    ]
    for i, person_dict in enumerate(people):
        if person_dict.get("wife") is not None:
            result[i].wife = Person.people[person_dict["wife"]]
        if person_dict.get("husband") is not None:
            result[i].husband = Person.people[person_dict["husband"]]
    return result
