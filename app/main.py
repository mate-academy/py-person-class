class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_instances = [
        Person(person["name"],
               person["age"])
        for person in people
    ]

    for person_instance in person_instances:
        person_data = next(
            (person for person in people if person["name"]
             == person_instance.name),
            None)

        if person_data.get("wife"):
            person_instance.wife = Person.people.get(person_data["wife"])
        if person_data.get("husband"):
            person_instance.husband = Person.people.get(person_data["husband"])

    return person_instances
