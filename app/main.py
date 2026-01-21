class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def __repr__(self) -> str:
        return f"name={self.name!r}, age={self.age!r}"


def create_person_list(people: list[dict]) -> list:
    # Clear global dict before create new objects
    Person.people.clear()

    for person in people:
        current_person = Person(person["name"], person["age"])
        spouse_key = "wife" if "wife" in person else "husband"
        spouse_name = person[spouse_key]
        if spouse_name in Person.people:
            spouse = Person.people[spouse_name]
            setattr(current_person, spouse_key, spouse)
            setattr(spouse, "wife" if spouse_key == "husband"
                    else "husband", current_person)

    return list(Person.people.values())
