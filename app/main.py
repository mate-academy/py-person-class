
class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []

    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        result.append(Person(name, age))

    for person_data in people:
        if person_data.get("husband"):
            husband = Person.people[person_data["husband"]]
            Person.people[person_data["name"]].husband = husband
        if person_data.get("wife"):
            wife = Person.people[person_data["wife"]]
            Person.people[person_data["name"]].wife = wife

    return result
