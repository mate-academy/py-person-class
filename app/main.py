class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    for person_data in people:
        new_person = Person(
            name=person_data["name"],
            age=person_data["age"],
        )

        wife_name = person_data.get("wife")
        husband_name = person_data.get("husband")

        if wife_name:
            spouse = Person.people.get(wife_name)
            if spouse:
                new_person.wife = spouse
                spouse.husband = new_person

        if husband_name:
            spouse = Person.people.get(husband_name)
            if spouse:
                new_person.husband = spouse
                spouse.wife = new_person

    return list(Person.people.values())
