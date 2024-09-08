class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
        self.people[name] = self


def create_person_list(people: list[dict[str, str | int]]) -> list[Person]:
    person_list: list[Person] = [
        Person(person_data["name"], person_data["age"])
        for person_data in people
    ]

    for person_data in people:
        person = Person.people[person_data["name"]]
        if person_data.get("wife"):
            person.wife = Person.people[person_data["wife"]]
            if person.wife:
                person.wife.husband = person

        if person_data.get("husband"):
            person.husband = Person.people[person_data["husband"]]
            if person.husband:
                person.husband.wife = person

    return person_list
