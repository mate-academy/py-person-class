class Person:
    people: dict = {}

    def __init__(self, name : str, age : int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_instances = [
        Person(person_data["name"], person_data["age"])
        for person_data in people
    ]
    for person_data, person in zip(people, person_instances):
        if person_data.get("wife"):
            person.wife = Person.people[person_data["wife"]]
        if person_data.get("husband"):
            person.husband = Person.people[person_data["husband"]]

    return person_instances
