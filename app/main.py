class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []

    for person1 in people:
        person_obj = Person(person1["name"], person1["age"])
        result.append(person_obj)

    for person2 in people:
        person_obj = Person.people[person2["name"]]

        if "wife" in person2 and person2["wife"] is not None:
            person_obj.wife = Person.people[person2["wife"]]

        if "husband" in person2 and person2["husband"] is not None:
            person_obj.husband = Person.people[person2["husband"]]

    return result
