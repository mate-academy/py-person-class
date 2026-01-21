class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    list_with_classes = [Person(p["name"], p["age"]) for p in people]

    for data in people:
        current_person = Person.people[data["name"]]
        wife_name = data.get("wife")
        if wife_name:
            current_person.wife = Person.people[wife_name]
        hus_name = data.get("husband")
        if hus_name:
            current_person.husband = Person.people[hus_name]

    return list_with_classes
