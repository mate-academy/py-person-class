class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(person["name"], person["age"])
        for person in people
    ]
    for i, person_data in enumerate(people):
        if person_data.get("wife"):
            person_list[i].wife = person_data["wife"]
        elif person_data.get("husband"):
            person_list[i].husband = person_data["husband"]

    for person in person_list:
        if hasattr(person, "wife"):
            person.wife = Person.people[person.wife]
        elif hasattr(person, "husband"):
            person.husband = Person.people[person.husband]
    return person_list
