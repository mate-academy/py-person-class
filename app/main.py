class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
        Person.people[name] = self

    def get_wife(self) -> None:
        return self.wife

    def get_husband(self) -> None:
        return self.husband


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = [
        Person(person_data["name"], person_data["age"])
        for person_data in people
    ]

    for person in person_list:
        for person_data in people:
            if person.name == person_data["name"]:
                if "wife" in person_data and person_data["wife"]:
                    person.wife = Person.people[person_data["wife"]]
                if "husband" in person_data and person_data["husband"]:
                    person.husband = Person.people[person_data["husband"]]

    return person_list
