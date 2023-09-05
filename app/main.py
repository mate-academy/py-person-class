class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = [
        Person(person["name"], person["age"]) for person in people
    ]
    for person in people:
        person_partner = person.get("wife") or person.get("husband")
        if person_partner:
            person_instance = Person.people[person["name"]]
            marriage_couple_instance = Person.people[person_partner]
            if "wife" in person:
                person_instance.wife = marriage_couple_instance
            if "husband" in person:
                person_instance.husband = marriage_couple_instance
    return person_list
