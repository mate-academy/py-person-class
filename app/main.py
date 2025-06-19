class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    result = {}

    for person_dict in people:
        name = person_dict["name"]
        age = person_dict["age"]
        person = Person(name, age)
        result[name] = person

    for person_dict in people:
        name = person_dict["name"]
        person = result[name]

        if "wife" in person_dict and person_dict["wife"] is not None:
            person.wife = result[person_dict["wife"]]
        if "husband" in person_dict and person_dict["husband"] is not None:
            person.husband = result[person_dict["husband"]]

    return [result[p["name"]] for p in people]
