class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for person_data in people:
        Person(name=person_data["name"], age=person_data["age"])
    for person_data in people:
        person = Person.people.get(person_data["name"])
        if "wife" in person_data:
            if person_data["wife"] in Person.people:
                person.wife = Person.people[person_data["wife"]]
        if "husband" in person_data:
            if person_data["husband"] in Person.people:
                person.husband = Person.people[person_data["husband"]]
    return list(Person.people.values())
