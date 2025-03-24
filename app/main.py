class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()

    for person_data in people:
        Person(person_data["name"], person_data["age"])

    for person_data in people:
        current_person = Person.people[person_data["name"]]

        if person_data.get("wife"):
            current_person.wife = Person.people[person_data["wife"]]

        if person_data.get("husband"):
            current_person.husband = Person.people[person_data["husband"]]

    return [Person.people[p["name"]] for p in people]
