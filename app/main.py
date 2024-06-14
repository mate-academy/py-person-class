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


def create_person_list(people: list[dict[str, str]]) -> list[Person]:
    people_dict = [
        Person(person["name"], int(person["age"])) for person in people
    ]
    for person_data in people:
        if person_data.get("wife"):
            Person.people[person_data.get("name")].wife = Person.people[person_data.get("wife")]
        if person_data.get("husband"):
            Person.people[person_data.get("name")].husband = Person.people[person_data.get("husband")]
    return people_dict
