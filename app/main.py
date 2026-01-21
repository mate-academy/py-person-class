class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def __repr__(self) -> None:
        return f"Person: {self.name}, {self.age}"


def create_person_list(people_list: list) -> list:
    people_instances = []
    for person_data in people_list:
        name = person_data["name"]
        age = person_data["age"]
        people_instances.append(Person(name, age))

    for person_data in people_list:
        name = person_data["name"]
        person = Person.people.get(name)
        if person_data.get("wife"):
            person.wife = Person.people.get(person_data["wife"])
        if person_data.get("husband"):
            person.husband = Person.people.get(person_data["husband"])
    return people_instances
