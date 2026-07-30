class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list) -> list:
    for person_data in people_data:
        Person(person_data["name"], person_data["age"])

    for person_data in people_data:
        person = Person.people[person_data["name"]]
        if person_data.get("wife"):
            person.wife = Person.people[person_data["wife"]]
        elif person_data.get("husband"):
            person.husband = Person.people[person_data["husband"]]

    return list(Person.people.values())
