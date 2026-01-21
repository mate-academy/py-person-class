class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name, self.age = name, age
        self.people[name] = self


def create_person_list(people: list[dict]) -> list[dict]:
    for person_data in people:
        Person(name=person_data["name"], age=person_data["age"])

    for person_data in people:
        if person_data.get("wife"):
            Person.people[person_data["name"]].wife = (
                Person.people[person_data["wife"]])
            Person.people[person_data["wife"]].husband = Person.people[
                person_data["name"]
            ]
    return list(Person.people.values())
