class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    for person_data in people:
        person = Person(person_data["name"], person_data["age"])
        result.append(person)
    for person_data in people:
        person = Person.people[person_data["name"]]
        if person_data.get("wife"):
            person.wife = Person.people[person_data["wife"]]
        if person_data.get("husband"):
            person.husband = Person.people[person_data["husband"]]
    return result
