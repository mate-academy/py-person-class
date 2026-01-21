class Person:

    people = {}

    def __init__(
        self,
        name: str,
        age: int,
    ) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def __repr__(self) -> str:
        return f"Person: {self.name}, age: {self.age}"


def create_person_list(people: list) -> list[Person]:
    persons_instances = [
        Person(person.get("name"), person.get("age"))
        for person in people
    ]
    for person_dict in people:
        person = Person.people.get(person_dict["name"])
        if person_dict.get("wife"):
            person.wife = Person.people.get(person_dict["wife"])
        if person_dict.get("husband"):
            person.husband = Person.people.get(person_dict["husband"])

    return persons_instances
