class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    persons = [
        Person(person_data["name"], person_data["age"])
        for person_data in people
    ]
    for person_instance in people:
        person = Person.people[person_instance["name"]]
        if person_instance.get("wife"):
            person.wife = Person.people[person_instance["wife"]]
        elif person_instance.get("husband"):
            person.husband = Person.people[person_instance["husband"]]
    return persons
