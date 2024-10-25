class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self

    def __repr__(self) -> str:
        return (
            f"Person(name={self.name}, "
            f"age={self.age}, "
            f"wife={self.wife and self.wife.name}, "
            f"husband={self.husband and self.husband.name})"
        )


def create_person_list(people: list) -> list:
    persons_list = [Person(data["name"], data["age"]) for data in people]
    for data in people:
        person = Person.people[data["name"]]
        if "wife" in data and data["wife"]:
            person.wife = Person.people.get(data["wife"])
        if "husband" in data and data["husband"]:
            person.husband = Person.people.get(data["husband"])

    return persons_list
