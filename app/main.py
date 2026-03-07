class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people = {}

    person_list = [
        Person(person_data["name"], person_data["age"])
        for person_data in people
    ]

    for person_data in people:
        person = Person.people[person_data["name"]]

        if person_data.get("wife"):
            person.wife = Person.people[person_data["wife"]]

        husband_name = person_data.get("husband")
        if husband_name:
            person.husband = Person.people[person_data["husband"]]

    return person_list
